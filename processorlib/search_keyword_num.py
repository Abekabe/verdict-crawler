#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def search_keyword_num(content, keyword, date, file_num, filename):

    try:
        find_list = re.findall(keyword, content)
        find_num = len(find_list)
    except:
        find_num = '*'

    find_list.insert(0, file_num)

    # save csv file
    filepath = 'analysis_' + date + '/search_' + filename  + '_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '出現次數'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num, find_num])

    return find_num
