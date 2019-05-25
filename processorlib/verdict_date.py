#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def get_verdict_date(verdict, date, file_num):

    try:
        verdict = verdict.replace('\n', '')
        index = [m.start() for m in re.finditer('書記官', verdict)]
        verdict = verdict[:index[-1]]
        end_index = verdict.index('中華民國', len(verdict) - 100)
        verdict_date = verdict[end_index + 4: verdict.index('日', end_index) + 1]
        year = verdict_date[:verdict_date.index('年')]
        mouth = verdict_date[verdict_date.index('年') + 1 : verdict_date.index('月')]
        day = verdict_date[verdict_date.index('月') + 1 : verdict_date.index('日')]
        date_list = [year, mouth, day]
    except:
        date_list = ['*', '*', '*']

    # save csv file
    filepath = 'analysis_' + date + '/verdict_date_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '判決年', '判決月', '判決日'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num, date_list[0], date_list[1], date_list[2]])

    return date_list
