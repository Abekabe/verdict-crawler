#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_plain_content(verdict, date, file_num):
    '''
    try:
        start_index = verdict.index('\n二、')
        end_index = verdict.index('\n三、', start_index)
        content = verdict[start_index + 5 : end_index].replace('\n', '')
        content_num = len(content)
    except:
        content = '*'
        content_num = '*'
    '''
    content = ''
    content_line = verdict.replace('\n二、', '@').replace('\n三、', '@').replace('\n四、', '@').replace('\n五、', '@').split('@')
    for line in content_line:
        if line[:5].find('原告') != -1:
            content = line
            content_num = len(content)

    if content == '':
        content = '*'
        content_num = -1

    # save csv file
    filepath = 'analysis_' + date + '/plain_content_num_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '原告字數'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,content_num])

    return content[0], content_num
