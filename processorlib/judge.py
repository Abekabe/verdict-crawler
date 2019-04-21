#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_judge(verdict, date, file_num):
    judge = ''
    end_index = verdict.index('中華民國', len(verdict) - 1200)
    result_line = verdict[end_index: end_index + 50].split('\n')
    for line in result_line:
        if line.find('法官') != -1:
            judge += line[line.index('法官') + 2:] + '、'
    judge = judge[:-1]

    #print(judge)

    # save csv file
    filepath = 'analysis_' + date + '/judge_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '法官'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,judge])

    return judge
