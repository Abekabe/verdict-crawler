#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_reason_content_litigation(verdict, date, file_num):

    try:
        start_index = verdict.index('一、')
        end_index = verdict.index('二、', start_index)
        content = verdict[start_index + 5 : end_index].replace('\n', '')
        content_num = len(content)

    except:
        content = '*'
        content_num = '*'


    # save csv file
    filepath = 'analysis_' + date + '/reason_content_num_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '事實字數'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,content_num])

    return content, content_num
