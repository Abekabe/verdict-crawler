#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def get_total_content(verdict, date, file_num):

    try:

        index = [m.start() for m in re.finditer('書記官', verdict)]
        verdict = verdict[:index[-1]]
        end_index = verdict.index('中華民國', len(verdict) - 1000)
        verdict = verdict[verdict.index('理由'):end_index]
        content_num = len(verdict)

    except:
        content_num = '*'

    # save csv file
    filepath = 'analysis_' + date + '/總字數_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '總字數'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,content_num])

    return  content_num
