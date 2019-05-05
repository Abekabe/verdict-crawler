#!/usr/bin/env python
# coding: utf-8
import os
import csv

def get_debate_end_simple(verdict, date, file_num):

    try:
        set_line = verdict[:verdict.index('上列當事人')]
        end_index = set_line.index('辯論終結')
        end_date = set_line[set_line.index('號', end_index - 20) + 2 : end_index]
        year = end_date[:end_date.index('年')]
        mouth = end_date[end_date.index('年') + 1 : end_date.index('月')]
        day = end_date[end_date.index('月') + 1 : end_date.index('日')]
        date_list = [year, mouth, day]

    except:
        date_list = ['*', '*', '*']

    # save csv file
    filepath = 'analysis_' + date + '/debate_end_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '辯論終結年', '辯論終結月', '辯論終結日'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_num, date_list[0], date_list[1], date_list[2]])

    return date_list

