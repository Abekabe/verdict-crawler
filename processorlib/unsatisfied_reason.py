#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_unsatisfied_reason(verdict, date, file_num):
    verdict = verdict.replace('\n', '')
    start_index = verdict.index('中華民國') + 4
    start_index = verdict.index('日', start_index)
    reason = verdict[start_index + 1 : verdict.index('，', start_index)]
    #print(verdict[start_index - 50 : start_index + 51])
    #print(reason)

    # save csv file
    filepath = 'analysis_' + date + '/unsatisfied_reason_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '不服訴願原因'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,reason])

    return reason
