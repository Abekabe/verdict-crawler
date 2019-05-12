#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re
chs_arabic_map = {u'零':0, u'一':1, u'二':2, u'三':3, u'四':4, u'五':5, u'六':6, u'七':7, u'八':8, u'九':9, u'十':10,}

def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def get_verdict_result(verdict, date, file_num):

    try:
        result = ['0', '0', '0', '']
        end_index = verdict.index('。', verdict.index('理由') - 10)
        result_line = verdict[verdict.index('主文') + 2: end_index].replace('\n', '')
        if result_line.find('駁回') != -1:
            result[1] = '1'
        if result_line.find('撤銷') != -1:
            result[0] = '1'
        if result_line.find('廢棄') != -1:
            result[2] = '1'
        if result_line.find('訴訟費用') != -1:
            index = [m.start() for m in re.finditer('訴訟費用', result_line)]
            re_line = result_line[index[-1]:]
            m = re.match('訴訟費用[^，由]*由([被原])?[告上訴人]{1,3}負擔(.*，)?', re_line)
            if (m.group(2) != None):
                num = re.split('/|分之|分', m.group(2)[:-1])
                if m.group(2).find('/') != -1:
                    ind = [0, 1]
                else:
                    ind = [1, 0]
                if (is_number(num[0])):
                    number = int(num[ind[0]]) / int(num[ind[1]])
                else:
                    number = chs_arabic_map[num[ind[0]]] / chs_arabic_map[num[ind[1]]]
            else:
                number = 1
            if (m.group(1) != '被'):
                number = 1 - number

            result[3] = str(number)

        main_text = result_line

    except:
        result = ['*', '*', '*', '*']
        main_text = '*'

    result.insert(0, file_num)

    # save csv file
    filepath = 'analysis_' + date + '/判決結果_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '判決結果'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(result)

    # save csv file
    filepath = 'analysis_' + date + '/判決主文_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '判決主文'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([file_num, main_text])

    return result[1:], main_text
