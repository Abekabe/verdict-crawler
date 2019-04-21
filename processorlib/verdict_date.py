#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_verdict_date(verdict, date, file_num):

    verdict = verdict.replace('\n', '')
    end_index = verdict.index('中華民國', len(verdict) - 1000)
    verdict_date = verdict[end_index + 4: verdict.index('日', end_index) + 1]
    #print(verdict_date)

    # save csv file
    filepath = 'analysis_' + date + '/verdict_date_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '判決日期'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,verdict_date])

    return verdict_date
