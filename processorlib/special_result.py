#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_special_result(verdict, date, file_num):

    try:
        result_line = verdict[verdict.index('主文'): verdict.index('。', verdict.index('主文'))].replace('\n', '')
        if result_line.find('元') != -1:
            result = '是'
        else:
            result = '否'

    except:
        result = '*'
    #print(result)

    # save csv file
    filepath = 'analysis_' + date + '/special_result_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '自為判決'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,result])

    return result
