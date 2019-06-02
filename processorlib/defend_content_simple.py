#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def get_defend_content_simple(verdict, date, file_num):

    try:
        content = ''

        title = re.search("^\S、\S*(?:被上訴|被告).{0,6}(?:略以|則以|主張|抗辯|答辯|辯以)\S*(?:︰|：)", verdict, re.M).group(0)
        number_list = ['一', '二' ,'三', '四', '五']
        if any(num in title for num in number_list):
            content_line = re.split('\n一、|\n二、|\n三、|\n四、|\n五、|\n壹、|\n貳、|\n參、|\n肆、|\n伍、' ,verdict)
        else:
            content_line = re.split('\n壹、|\n貳、|\n參、|\n肆、|\n伍、' ,verdict)
        for line in content_line:
            if (re.search("^\S*(?:被上訴|被告).{0,6}(?:略以|則以|主張|抗辯|答辯|辯以)\S*(?:︰|：)", line, re.M) != None):
                content = line.replace(' ', '')
                content_num = len(content)
                break;

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
