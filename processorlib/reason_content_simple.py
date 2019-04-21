#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_reason_content_simple(verdict, date, file_num):

    start_index = verdict.index('事實概要')
    end_index = verdict.index('。', verdict.index('原告主張', start_index) - 10) + 1
    content = verdict[start_index + 5 : end_index].replace('\n', '')

    #print(file_num)
    #print(len(content))

    content_num = len(content)
    '''
    # save csv file
    filepath = 'analysis_' + date + '/reason_content_num_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '事實字數'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,content_num])
    '''
    return content, content_num
