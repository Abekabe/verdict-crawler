#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_verdict_result(verdict, date, file_num):

    try:
        result = ['否', '否', '否', '']
        end_index = verdict.index('。', verdict.index('理由') - 10)
        result_line = verdict[verdict.index('主文') + 2: end_index].replace('\n', '')
        if result_line.find('駁回') != -1:
            result[1] = '是'
        if result_line.find('撤銷') != -1:
            result[0] = '是'
        if result_line.find('廢棄') != -1:
            result[2] = '是'
        if result_line.find('訴訟費用') != -1:
            result[3] = result_line[result_line.index('訴訟費用'):]
        main_text = result_line
    except:
        result = ['*', '*', '*', '*']
        main_text = '*'
    #print(result)
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
