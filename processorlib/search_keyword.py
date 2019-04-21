#!/usr/bin/env python
# coding: utf-8
import os
import csv

def search_keyword(content, keyword, date, file_num, filename):

    if content.find(keyword) != -1:
        find = '有'
    else:
        find = '無'


    # save csv file
    filepath = 'analysis_' + date + '/search_' + filename  + '_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '搜尋結果'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,find])

    return find
