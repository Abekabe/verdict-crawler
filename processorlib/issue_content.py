#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def get_issue_content(verdict, date, file_num):

    try:
        content = ''
        index = [m.start() for m in re.finditer('書記官', verdict)]
        verdict = verdict[:index[-1]]
        end_index = verdict.index('高等行政法院', len(verdict) - 3000)
        verdict = verdict[:end_index]
        title = re.search("^\S、\S*(?:上訴|原告).{0,6}(?:主張|意旨)\S*(?:︰|：)", verdict, re.M).group(0)
        number_list = ['一', '二' ,'三', '四', '五', '六', '七']
        if any(num in title for num in number_list):
            content_line = re.split('\n一、|\n二、|\n三、|\n四、|\n五、|\n六、|\n七、|\n壹、|\n貳、|\n參、|\n肆、|\n伍、' ,verdict)
        else:
            content_line = re.split('\n壹、|\n貳、|\n參、|\n肆、|\n伍、|\n陸、|\n柒、' ,verdict, re.M)
        plain_index, defend_index = 0, 0
        for num in range(len(content_line)):
            if (re.search("^\S*(?:上訴|原告).{0,6}(?:主張|意旨)\S*(?:︰|：)", content_line[num], re.M) != None):
                plain_index = num
                break;

        for num in range(len(content_line)):
            if (re.search("^\S*(?:被上訴|被告).{0,6}(?:略以|則以|主張|抗辯|答辯|辯以)\S*(?:︰|：)", content_line[num], re.M) != None):
                defend_index = num
                break;

        remain_content = content_line[max(plain_index, defend_index)+1]
        start_index = [m for m in re.finditer('爭.{0,5}點[\s\S]{0,1000}？', remain_content)][-1]
        remain_content = remain_content[start_index.start(): start_index.end()]
        end_index = re.search("如下", remain_content, re.M)
        if (end_index != None):
            content = remain_content[:end_index.start() + 2]
            issue_end = end_index.start() + 2
        else:
            content = remain_content
            issue_end = start_index.end()

        content_num = len(content)
        if content == '':
            content = '*'
            content_num = -1

    except:
        content = ''
        content_num = '*'
        issue_end = 0

    # save csv file
    filepath = 'analysis_' + date + '/issue_content_num_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '爭點字數'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,content_num])

    return content, content_num, issue_end
