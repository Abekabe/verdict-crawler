#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_plain_represent_litigation(verdict, date, file_num):

    line = verdict.split('被上訴人')[0].split('上訴人')[1].replace('\n', '').replace('共同', '')

    if line.find('代表人') != -1:
        if line.find('訴訟代理人') != -1:
            plain_represent = line.split('訴訟代理人')[0][line.index('代表人') + 3:]
        else:
            plain_represent = line[line.index('代表人') + 3:]
    else:
        plain_represent = ''

    #print(plain_represent)

    # save csv file
    filepath = 'analysis_' + date + '/plain_represent_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '上訴人代表人'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,plain_represent])

    return plain_represent
