#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def get_judge(verdict, date, file_num):

    try:
        judge_list = []
        index = [m.start() for m in re.finditer('書記官', verdict)]
        verdict = verdict[:index[-1]]
        end_index = verdict.index('中華民國', len(verdict) - 1000)
        result_line = verdict[end_index: end_index + 50].split('\n')
        for line in result_line:
            if line.find('法官') != -1:
                judge_list.append(line[line.index('法官') + 2:])

    except:
        judge_list = ['*']

    judge_list.insert(0, file_num)
    judge = '、'.join(judge_list[1:])

    # save csv file
    filepath = 'analysis_' + date + '/judge_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '法官'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(judge_list)

    return judge
