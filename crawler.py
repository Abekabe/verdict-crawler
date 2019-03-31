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

s = requests.Session()
r = s.post(domain + 'indexContent_1.aspx', data = payload)
soup = BeautifulSoup(r.text, 'html.parser')
search = soup.find_all('frame')[1].get('src')


payload = {'v_sys': 'A',
            'courtFullName': 'TPBA',
            'jud_title': '所得稅',
            'sdate': start,
            'edate': end          }

h = {'Referer': domain + 'indexContent_1.aspx'}

r = s.post(domain + search, data = payload, cookies = r.cookies, headers = h)
soup = BeautifulSoup(r.text, 'html.parser')
verdicts = soup.find_all('a')
total_num = soup.find_all(attrs={'width':"42%", 'valign':"middle", 'align':"center"})[1].text.split('\n')[1].strip()
print('total: ' + str(total_num))

for verdict in verdicts:
    link = verdict.get('href')
    if not link.find('FJUDQRY03_1.aspx') :
        padding = link.split('id=1')
        break

soup = BeautifulSoup(r.text, 'html.parser')
verdicts = soup.find_all('a')
h = {'Referer': domain + search}
data = []
with open('output.csv', 'w', encoding = 'utf-8') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerow(['id', 'number', 'date', 'reason', 'content'])
    writer.writerow(['id', 'number', 'date', 'reason'])
    verdict_list = list(range(int(total_num)))
    while verdict_list != []:
        verdict_id = int(verdict_list[0]) + 1
        try:
            link = padding[0] + 'id=' + str(verdict_id) + padding[1]
            r = s.post(domain + link, data = payload, cookies = r.cookies, headers = h)
            soup = BeautifulSoup(r.text, 'html.parser')
            verdict_content = soup.find('td', id='jfull').text
            detail = soup.find_all('span')  
            title = detail[3].text[8:]
            verdict_num = detail[3].text[8:]
            verdict_date = detail[4].text[8:]
            verdict_reason = detail[5].text[8:]
            #data.append([verdict_id, verdict_num, verdict_date, verdict_reason, verdict_content])
            data.append([verdict_id, verdict_num, verdict_date, verdict_reason])
            print(data[-1][0])
            path = "data/"
            if not os.path.isdir(path):
                os.mkdir(path)
            f = open('data/' + title + '.txt','wb+')
            f.write(verdict_content.encode("utf8"))
            verdict_list.pop(0)
            
        except AttributeError:
            print('AttributeError in ' + str(verdict_id))          
        except ConnectionError:
            print('Connection aborted in ' + str(verdict_id))
            
        time.sleep(3)

    sorted(data, key = lambda x : x[0])
    for item in data:
        writer.writerow(item)