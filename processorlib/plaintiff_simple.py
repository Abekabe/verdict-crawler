#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_plaintiff_simple(verdict, date, file_num):

    line = verdict.split('原告')[1].split('被告')[0].replace('\n', '').replace('共同', '')

    if line.find('代表人') != -1:
        line = line.replace('代表人', '@')
    if line.find('訴訟代理人') != -1:
        line = line.replace('訴訟代理人', '@')

    line = line.split('@')
    plaintiff = line[0]

    #print(plaintiff)

    # save csv file
    filepath = 'analysis_' + date + '/plaintiff_simple_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '原告'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,plaintiff])

    return plaintiff
