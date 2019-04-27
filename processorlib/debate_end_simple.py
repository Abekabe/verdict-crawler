#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_debate_end_simple(verdict, date, file_num):

    try:
        set_line = verdict[:verdict.index('上列當事人')]
        end_index = set_line.index('辯論終結')
        end_date = set_line[set_line.index('號', end_index - 20) + 2 : end_index]
    except:
        end_date = '*'

    # save csv file
    filepath = 'analysis_' + date + '/debate_end_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '辯論終結日期'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num,end_date])

    return end_date

