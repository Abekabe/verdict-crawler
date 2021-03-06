#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_plain_content_litigation(verdict, date, file_num):

    try:
        content = ''
        if verdict.find('\n壹、') != -1 and verdict.find('壹、程序部分') == -1:
            content_line = verdict.replace('\n貳、', '@').replace('\n參、', '@').replace('\n肆、', '@').split('@')
        else:
            content_line = verdict.replace('\n二、', '@').replace('\n三、', '@').replace('\n四、', '@').split('@')
        for line in content_line:
            if line.find('上訴') == 0 and len(line) > 100:
                content = line
                content_num = len(content)

        if content == '':
            content = '*'
            content_num = -1

    except:
        content_num = '*'

    # save csv file
    filepath = 'analysis_' + date + '/plain_content_num_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '原告字數'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,content_num])

    return content, content_num
