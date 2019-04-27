#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_unsatisfied_date(verdict, date, file_num):

    try:
        start_index = verdict.index('中華民國') + 4
        unsatisfied_date = verdict[start_index : verdict.index('日', start_index) + 1].replace('\n', '')

    except:
        unsatisfied_date = ''
    #print(unsatisfied_date)

    # save csv file
    filepath = 'analysis_' + date + '/unsatisfied_date_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '不服訴願日期'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,unsatisfied_date])

    return unsatisfied_date
