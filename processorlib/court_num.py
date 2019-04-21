#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_court_num(verdict, date, file_num):

    end_index = verdict.index('中華民國', len(verdict) - 1200)
    result_line = verdict[end_index: end_index + 50].split('\n')
    for line in result_line:
        if line.find('臺北高等行政法院') != -1:
            court_num = line[-2]

    #print(court_num)

    # save csv file
    filepath = 'analysis_' + date + '/court_num_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '法院幾庭'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,court_num])

    return court_num
