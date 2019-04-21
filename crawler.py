#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re
import csv
import time
import os

start = input("start(yyyymmdd): ")
end = input("end(yyyymmdd): ")

def get_url(domain, payload):
    s = requests.Session()
    r = s.post(domain + 'indexContent_1.aspx', data = payload)
    soup = BeautifulSoup(r.text, 'html.parser')
    search = soup.find_all('frame')[1].get('src')

    payload = {'v_sys': 'A',
                'courtFullName': 'TPBA',
                'jud_title': '所得稅',
                'sdate': start,
                'edate': end
            }

    h = {'Referer': domain + 'indexContent_1.aspx'}

    r = s.post(domain + search, data = payload, cookies = r.cookies, headers = h)
    soup = BeautifulSoup(r.text, 'html.parser')
    verdicts = soup.find_all('a')
    total_num = soup.find_all(attrs={'width':"42%", 'valign':"middle", 'align':"center"})[1].text.split('\n')[1].strip()
    print('total: ' + str(total_num))

    for verdict in verdicts:
        link = verdict.get('href')
        if link.find('FJUDQRY03_1.aspx') != -1:
            padding = link.split('id=1')
            break
    soup = BeautifulSoup(r.text, 'html.parser')
    verdicts = soup.find_all('a')
    h = {'Referer': domain + search}

    return padding, h, total_num, r, s

def save_content(num, padding, verdict_list, r):
    verdict_id = int(verdict_list[0]) + 1
    data = []
    try:
        link = padding[0] + 'id=' + str(verdict_id) + padding[1]
        s = requests.Session()
        r = s.post(domain + link, data = payload, cookies = r.cookies, headers = h)
        soup = BeautifulSoup(r.text, 'html.parser')
        verdict_content = soup.find('td', id='jfull').text
        detail = soup.find_all('span')
        verdict_num = detail[3].text[8:]
        verdict_date = detail[4].text[8:]
        verdict_reason = detail[5].text[8:]
        title = verdict_content.split('\n')[0]
        if title.find('判決') != -1:
            data = [num, verdict_num, verdict_date, verdict_reason]
            print(data[0])
            path = 'data_' + start + '_' + end + '/'
            if not os.path.isdir(path):
                os.mkdir(path)
            f = open(path + str(num) + '.txt','wb+')
            f.write(verdict_content.encode("utf-8"))
            verdict_list.pop(0)
            #num += 1
        else:
            verdict_list.pop(0)
    except AttributeError:
        print('AttributeError in ' + str(verdict_id))
    except ConnectionError:
        print('Connection aborted in ' + str(verdict_id))

    return data

if __name__ == '__main__':
    domain = 'http://jirs.judicial.gov.tw/FJUD/'
    payload = {'v_court':'TPB 臺北高等行政法院',
               'v_sys':'A',
               'sel_judword':'常用字別',
               'jt':'所得稅',
               'Button':'查詢',
               'jud_title':'所得稅',
               'courtFullName':'TPBA',
               'sdate': start,
               'edate': end
              }

    padding, h, total_num, r, s = get_url(domain, payload)
    filepath = 'catalog_' + start + '_' + end + '.csv'

    exist_num = [-1]
    data = []
    '''
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding = 'big5', newline='\n') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            exist_num.extend(list(int(row[0]) for row in reader))
            data.append(list(row for row in reader))
        num = exist_num[-1]
        csvfile.close()
    else:
        num = 1
    while [] in data:
            data.remove([])
    '''
    with open(filepath, 'w', encoding = 'big5', newline='\n') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'number', 'date', 'reason'])
        verdict_list = list(range(int(total_num)))
        (verdict_list.remove(x) for x in exist_num)
        print(verdict_list)

        while verdict_list != []:
            d = save_content(len(data) + 1, padding, verdict_list, r)
            if d != []:
                data.append(d)
            time.sleep(1)
        sorted(data, key = lambda x : x[0])
        writer.writerows(data)

    csvfile.close()
    print(str(len(data)) + '/' + total_num)
    input('Success!! Please press any key to continue...')
