#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_defend_represent_simple(verdict, date, file_num):

    try:
        line = verdict[verdict.index('被告') + 2 : verdict.index('上列當事人')].replace('\n', '')

        if line.find('代表人') != -1:
            if line.find('訴訟代理人') != -1:
                defend_represent = line.split('訴訟代理人')[0][line.index('代表人') + 3:]
            else:
                defend_represent = line[line.index('代表人') + 3:]
        else:
            defend_represent = ''
    except:
        defend_represent = '*'
    #print(defend_represent)

    # save csv file
    filepath = 'analysis_' + date + '/defend_represent_simple_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '被告代表人'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,defend_represent])

    return defend_represent
