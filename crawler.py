#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re
import csv
import time
import os
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_views(url):
    r = requests.get(url, verify=False)
    bs = BeautifulSoup(r.text, 'html.parser')
    state = bs.find("input", {"id": "__VIEWSTATE"}).attrs['value']
    generator = bs.find("input", {"id": "__VIEWSTATEGENERATOR"}).attrs['value']
    eventvalidation = bs.find("input", {"id": "__EVENTVALIDATION"}).attrs['value']
    return [state, generator, eventvalidation]

def get_url(domain, payload):

    h = {'Referer': domain + 'default.aspx'}
    s = requests.Session()
    r = s.post(domain + 'default.aspx/', data = payload, verify=False, headers = h)
    soup = BeautifulSoup(r.text, 'html.parser')
    search = soup.find('iframe').get('src')
    r = s.post(domain + search, cookies = r.cookies, verify=False, headers = h)
    soup = BeautifulSoup(r.text, 'html.parser')
    padding = soup.find_all(attrs={"id" : "hlTitle", "class" : "hlTitle_scroll"})[1].get('href').split('ro=1')
    total_line = soup.find('span').text
    total_num = int(total_line[total_line.index('共') + 2 : total_line.index('筆') - 1]) - 1

    return padding, h, total_num, r, search

def save_content(num, padding, verdict_list, r, search):
    verdict_id = int(verdict_list[0]) + 1
    data = []
    try:
        link = padding[0] + 'ro=' + str(verdict_id) + padding[1]
        s = requests.Session()
        h = {'Referer': domain + link}
        r = s.post(domain + link, cookies = r.cookies, verify=False, headers = h)
        soup = BeautifulSoup(r.text, 'html.parser')
        verdict_content = soup.find(attrs={"class" : "text-pre text-pre-in"}).text
        detail = soup.find_all(attrs={"class" : "col-td"})
        verdict_num = detail[0].text
        verdict_date = detail[1].text
        verdict_reason = detail[2].text
        title = verdict_content.split('\n')[0]
        if title.find('判決') != -1:
            data = [num, str(verdict_id), verdict_num, verdict_date, verdict_reason]
            path = 'data_' + start + '_' + end + '/'
            if not os.path.isdir(path):
                os.mkdir(path)
            f = open(path + str(num) + '.txt', 'wb+')#, encoding = 'big5')
            f.write(verdict_content.encode("big5", "replace").decode("big5").encode("utf-8"))#
            verdict_list.pop(0)
            print(data[0])
            num += 1
        else:
            verdict_list.pop(0)
    except AttributeError:
        print('AttributeError in ' + str(verdict_id))
    except ConnectionError:
        print('Connection aborted in ' + str(verdict_id))

    return data, num

if __name__ == '__main__':
    start = input("start(yyymmdd): ")
    end = input("end(yyymmdd): ")
    domain = 'https://law.judicial.gov.tw/FJUD/'
    views = get_views(domain + 'default.aspx/')
    court_list = ['TPB', 'TCB', 'KSB']
    court_name = {'臺北': 'TPB', '臺中': 'TCB', '高雄': 'KSB'}
    filepath = 'catalog_' + start + '_' + end + '.csv'
    exist_num = []
    exist_id = []
    exist_court = []

    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding = 'big5', newline='\n') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                exist_num.append(int(row[0]))
                exist_id.append(int(row[1]))
                exist_court.append(row[2])
            #data.append(list(row for row in reader))
        print(exist_id)
        current_num = exist_num[-1] + 1
        current_id = exist_id[-1]
        court_num = court_list.index(court_name[exist_court[-1][:2]])
        csvfile.close()
    else:
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['num', 'id', 'number', 'date', 'reason'])
        current_num = 1
        current_id = 0
        court_num = 0

    for num in range(court_num, len(court_list)):
        payload = {'jud_court': court_list[num],
                    'jud_sys': 'A',
                   'sel_judword':'常用字別',
                   'judtype': 'JUDBOOK',
                    'whosub': '1',
                    'ctl00$cp_content$btnQry': '送出查詢',
                    'dy1': start[:-4],
                    'dm1': start[-4:-2],
                    'dd1': start[-2:],
                    'dy2': end[:-4],
                    'dm2': end[-4:-2],
                    'dd2': end[-2:],
                    'jud_title': '所得稅',
                    '__VIEWSTATE': views[0],
                    '__VIEWSTATEGENERATOR': views[1],
                    '__EVENTVALIDATION': views[2]
                  }

        padding, h, total_num, r, search = get_url(domain, payload)

        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            verdict_list = list(range(int(current_id), int(total_num)))
            print(verdict_list)

            while verdict_list != []:
                d, current_num = save_content(current_num, padding, verdict_list, r, search)
                if d != []:
                    writer.writerow(d)
                time.sleep(1)

        csvfile.close()
        print(str(current_num) + '/' + str(total_num))
        current_id = 0
    input('Success!! Please press any key to continue...')
