#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def get_plain_content_simple(verdict, date, file_num):

    try:
        content = ''
        title = re.search("^\S、\S*(?:上訴|原告).{0,6}(?:主張|意旨)\S*(?:︰|：)", verdict, re.M).group(0)
        number_list = ['一', '二' ,'三', '四', '五']
        if any(num in title for num in number_list):
            content_line = re.split('\n一、|\n二、|\n三、|\n四、|\n五、' ,verdict)
        else:
            content_line = re.split('\n壹、|\n貳、|\n參、|\n肆、|\n伍、' ,verdict)

        for line in content_line:
            search_result = re.search("^\S*(?:上訴|原告).{0,6}(?:主張|意旨)\S*(?:︰|：)", line, re.M)
            if (search_result != None):
                content = line.replace(' ', '')
                content_num = len(content)
                break;


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
