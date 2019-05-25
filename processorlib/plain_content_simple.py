#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def get_plain_content_simple(verdict, date, file_num):

    try:
        content = ''

        if (re.search("\s壹、(?!程序)", verdict) != None):
            content_line = re.split('壹、|貳、|參、|肆、|伍、' ,verdict)
        else:
            content_line = re.split('一、|二、|三、|四、|五、' ,verdict)
        for line in content_line:
            if (int(file_num) == 42):
                print(line)
            if (re.search("(?:上訴人|原告).{0,4}(?:主張|意旨)\S*(?:︰|：)", line) != None):
                content = line
                content_num = len(content)
        '''
        start_index = re.search("(?:上訴人|原告).{0,4}(?:主張|意旨).*", verdict).start()
        start_content = verdict[verdict[start_index:].index('\n') + start_index:]
        end_index = re.search("聲\s{0,5}明[\s\S]*。", start_content).start() + start_index
        content = verdict[start_index: end_index]
        content_num = len(content)
        '''

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
