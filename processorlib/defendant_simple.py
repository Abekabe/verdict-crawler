#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_defendant_simple(verdict, date, file_num):

    try:
        line = verdict[verdict.index('被告') + 2 : verdict.index('上列當事人')].replace('\n', '')

        if line.find('代表人') != -1:
            line = line.replace('代表人', '@')
        if line.find('訴訟代理人') != -1:
            line = line.replace('訴訟代理人', '@')

        line = line.split('@')
        defendant = line[0]
    except:
        defendant = '*'
    #print(defendant)

    # save csv file
    filepath = 'analysis_' + date + '/defendant_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '被告'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,defendant])

    return defendant
