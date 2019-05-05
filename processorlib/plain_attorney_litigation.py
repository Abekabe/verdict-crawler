#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_plain_attorney_litigation(verdict, date, file_num):

    line = verdict.split('被上訴人')[0].split('上訴人')[1].replace('\n', '').replace('共同', '')

    if line.find('訴訟代理人') != -1:
        plain_attorney = line[line.index('訴訟代理人') + 5:]
    else:
        plain_attorney = ''

    if plain_attorney.find('會計師') != -1:
        plain_attorney = plain_attorney.replace('會計師', '會計師、')
    if plain_attorney.find('律師') != -1:
        plain_attorney = plain_attorney.replace('律師', '律師、')
    if plain_attorney.find('訴訟代理人') != -1:
        plain_attorney = plain_attorney.replace('訴訟代理人', '、')

    plain_attorney = plain_attorney[:-1]
    plain_attorney_list = plain_attorney.split('、')
    plain_attorney_list.insert(0, file_num)
    #print(plain_attorney_list)

    #print(plain_attorney)

    # save csv file
    filepath = 'analysis_' + date + '/plain_attorney_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '上訴人訴訟代理人'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(plain_attorney_list)

    return plain_attorney
