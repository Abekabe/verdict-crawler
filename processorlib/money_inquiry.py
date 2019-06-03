#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def get_money_inquiry(content, date, file_num):

    try:
        money = '*'
        leak_money = '*'
        content = content.replace('\n', '')
        money_list = []
        money_content = re.findall('(?:補徵|應[納補退])稅額(?:[0-9,]*元、)*[0-9,]*元', content)
        for c in money_content:
            money_list.extend([m.group(1) for m in re.finditer('([0-9,]*)元', c)])

        leak_money_list = []
        leak_money_content = re.findall('所漏稅額(?:[0-9,]*元、)*[0-9,]*元', content)
        for c in leak_money_content:
            leak_money_list.extend([m.group(1) for m in re.finditer('([0-9,]*)元', c)])

        money = '、'.join(money_list)
        leak_money = '、'.join(leak_money_list)

        if money == '':
            money = '*'
        if leak_money == '':
            leak_money = '*'

    except:
        money = '*'
        leak_money = '*'

    money_list.insert(0, file_num)
    leak_money_list.insert(0, file_num)
    # save csv file
    filepath = 'analysis_' + date + '/money_inquiry_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '補徵稅額'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(money_list)

    filepath = 'analysis_' + date + '/leak_money_inquiry_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '所漏稅額'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(leak_money_list)

    return money, leak_money
