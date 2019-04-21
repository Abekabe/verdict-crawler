#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_money_inquiry(content, date, file_num):
    content = content.replace('\n', '')
    if content.find('補徵稅額') != -1:
        start_index = content.index('補徵稅額')
        money = content[start_index + 4 : content.index('元', start_index) + 1]
        if len(money) > 20:
            money = ''
    else:
        money = ''
    #print(money)

    # save csv file
    filepath = 'analysis_' + date + '/money_inquiry_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '補徵稅額'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,money])

    return money
