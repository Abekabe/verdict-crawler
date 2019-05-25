#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def get_defend_content_simple(verdict, date, file_num):

    try:
        content = ''

        if (re.search("\s壹、(?!程序)", verdict) != None):
            content_line = re.split('壹、|貳、|參、|肆、|伍、' ,verdict)
        else:
            content_line = re.split('一、|二、|三、|四、|五、' ,verdict)
        for line in content_line:
            if (re.search("(?:被上訴人|被告).{0,4}(?:略以|則以|主張|抗辯|答辯)\S*(?:︰|：)", line) != None):
                content = line
                content_num = len(content)
        '''
        start_index = re.search("(?:被上訴人|被告).{0,4}(?:略以|則以|主張|抗辯|答辯).*", verdict).start()
        start_content = verdict[verdict[start_index:].index('\n') + start_index:]
        end_index = re.search("聲\s{0,5}明[\s\S]*。", start_content).start() + start_index
        content = verdict[start_index: end_index]
        content_num = len(content)
        '''
        #聲\s{0,5}明[\s\S]*。

        if content == '':
            content = '*'
            content_num = -1
    except:
        content_num = '*'


    # save csv file
    filepath = 'analysis_' + date + '/defend_content_num_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '被告字數'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,content_num])

    return content, content_num
