#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_verdict_result(verdict, date, file_num):

    result_line = verdict[verdict.index('主文'): verdict.index('。', verdict.index('主文'))].replace('\n', '')
    if result_line.find('駁回') != -1:
        result = '駁回'
    elif result_line.find('撤銷') != -1:
        result = '撤銷'
    elif result_line.find('廢棄') != -1:
        result = '廢棄'
    else:
        result = '????'
    #print(result)

    # save csv file
    filepath = 'analysis_' + date + '/verdict_result_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '判決結果'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,result])

    return result
