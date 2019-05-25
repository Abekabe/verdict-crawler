#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def get_result_content(verdict, date, file_num):

    try:
        content = ''
        index = [m.start() for m in re.finditer('書記官', verdict)]
        verdict = verdict[:index[-1]]
        end_index = verdict.index('中華民國', len(verdict) - 1000)
        verdict = verdict[:end_index]
        if verdict.find('\n壹、') != -1 and verdict.find('壹、程序部分') == -1:
            line = re.split('壹、|貳、|參、|肆、|伍、' ,verdict)
        else:
            line = re.split('一、|二、|三、|四、|五、' ,verdict)
        for num in range(len(line)):
            if (line[num][:5].find('被告') != -1 or line[num].find('被上訴') == 0) and len(line[num]) > 20:
                break
        if (num == len(line)-1):
            for num in range(len(line)):
                if (line[num][:5].find('原告') != -1 or line[num].find('上訴') == 0) and len(line[num]) > 20:
                    break
        content = ''.join(line[num+1:])
        #print(content)
        content_num = len(content)
        if content == '':
            content = '*'
            content_num = -1

    except:
        content_num = '*'

    # save csv file
    filepath = 'analysis_' + date + '/result_content_num_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '判斷字數'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,content_num])

    return content, content_num
