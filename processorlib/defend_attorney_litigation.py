#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_defend_attorney_litigation(verdict, date, file_num):

    try:
        line = verdict[verdict.index('被上訴人') + 4 : verdict.index('上列當事人')].replace('\n', '')

        if line.find('訴訟代理人') != -1:
            defend_attorney = line[line.index('訴訟代理人') + 5:]
        else:
            defend_attorney = ''

        if defend_attorney.find('會計師') != -1:
            defend_attorney = defend_attorney.replace('會計師', '會計師、')
        if defend_attorney.find('律師') != -1:
            defend_attorney = defend_attorney.replace('律師', '律師、')
        if defend_attorney.find('訴訟代理人') != -1:
            defend_attorney = defend_attorney.replace('訴訟代理人', '')

        defend_attorney_list = defend_attorney.split('、')
        defend_attorney_list.insert(0, file_num)
    except:
        defend_attorney = '*'
        defend_attorney_list = []
    #print(defend_attorney_list)

    # save csv file
    filepath = 'analysis_' + date + '/defend_attorney_litigation_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '被上訴人訴訟代理人'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(defend_attorney_list)

    return defend_attorney
