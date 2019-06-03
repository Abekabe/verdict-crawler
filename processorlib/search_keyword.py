#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re
from .chinese_digit import getResultForDigit

def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def search_keyword(content, keyword, date, file_num, filename, special):

    try:
        find_list = re.findall(keyword, content)
        find_list = list(set(find_list))
        find = '、'.join(find_list)

        # save csv file
        if (special == 1):
            l = []
            ans_head = ['3', '4', '5', '7', '9', '10', '11', '14', '16', '18', '21', '23']
            ans_list = ['0'] * len(ans_head)
            for item in find_list:
                m = re.match('納.*保.*法第(.*)條第{1,2}(.*)項', item)
                if (is_number(m.group(1))):
                    first = m.group(1)
                else:
                    first = getResultForDigit(m.group(1))
                if (is_number(m.group(2))):
                    second = m.group(2)
                else:
                    second = getResultForDigit(m.group(2))

                l.append(first + '-' + second)
                if first in ans_head:
                    ans_list[ans_head.index(first)] = '1'
            ans_list.insert(0, file_num)
            filepath = 'analysis_' + date + '/search_' + filename + '_條列' + '_' + date + '.csv'
            if not os.path.isfile(filepath):
                with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                    writer = csv.writer(csvfile)
                    ans_head.insert(0, '案件編號')
                    writer.writerow(ans_head)

            with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(ans_list)

        elif (special == 2):
            l = []
            ans_head = ['3', '4', '5', '7', '1']
            ans_list = ['0'] * len(ans_head)
            for item in find_list:
                m = re.match('稅捐稽徵法第([12十一二]{2})條?[之-]([1-7一三四五六七]{1})條?', item)
                if (is_number(m.group(1))):
                    first = m.group(1)
                else:
                    first = getResultForDigit(m.group(1))
                if (is_number(m.group(1))):
                    second = m.group(2)
                else:
                    second = getResultForDigit(m.group(2))
                l.append(first + '-' + second)

                if second in ans_head:
                    ans_list[ans_head.index(second)] = '1'

            ans_list.insert(0, file_num)
            filepath = 'analysis_' + date + '/search_' + filename + '_條列' + '_' + date + '.csv'
            if not os.path.isfile(filepath):
                with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                    writer = csv.writer(csvfile)
                    ans_h = ['11-3', '11-4', '11-5', '11-7', '12-1']
                    ans_h.insert(0, '案件編號')
                    writer.writerow(ans_h)

            with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(ans_list)

    except:
        find = '*'

    find_list.insert(0, file_num)
    filepath = 'analysis_' + date + '/search_' + filename  + '_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['案件編號', '搜尋結果'])

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(find_list)

    return find
