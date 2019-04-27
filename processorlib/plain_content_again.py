#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_plain_content_again(verdict, date, file_num):

    try:
        start_index = verdict.index('二、')
        end_index = verdict.index('三、', start_index)
        content = verdict[verdict.index('：', start_index) + 1 : end_index].replace('\n', '')
        content_num = len(content)
    except:
        content_num = '*'
    '''
    # save csv file
    filepath = 'analysis_' + date + '/plain_content_num_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '原告字數'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,content_num])
    '''
    return content_num
