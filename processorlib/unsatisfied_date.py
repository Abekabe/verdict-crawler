#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_unsatisfied_date(verdict, date, file_num):

    try:
        verdict = verdict.replace('\n', '')
        start_index = verdict.index('中華民國') + 4
        unsatisfied_date = verdict[start_index : verdict.index('日', start_index) + 1].replace('\n', '')
        year = unsatisfied_date[:unsatisfied_date.index('年')]
        mouth = unsatisfied_date[unsatisfied_date.index('年') + 1 : unsatisfied_date.index('月')]
        day = unsatisfied_date[unsatisfied_date.index('月') + 1 : unsatisfied_date.index('日')]
        date_list = [year, mouth, day]
    except:
        date_list = ['*', '*', '*']
    #print(unsatisfied_date)

    # save csv file
    filepath = 'analysis_' + date + '/unsatisfied_date_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '不服訴願年', '不服訴願月', '不服訴願日'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num, date_list[0], date_list[1], date_list[2]])

    return date_list
