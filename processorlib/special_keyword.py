#!/usr/bin/env python
# coding: utf-8
import os
import csv
import re

def search_special_keyword(content, date, file_num, filename):
    keyword1 = ['營利所得', '執行業務所得', '薪資所得', '利息所得', '租賃所得', '權利金所得', '自力耕作、漁、牧、林、礦之所得', '財產交易所得', '財產交易損失、競技、競賽及機會中獎之獎金或給與', '退職所得', '其他所得', '免稅額', '扣除額', '盈虧']
    keyword2 = ['收入', '成本', '費用', '損失', '營利事業所得額', '虧損', '投資收益', '估價', '  未分配盈餘']

    try:
        exist1 = [content.find(x) !=-1 for x in keyword1]
        exist2 = [content.find(x) !=-1 for x in keyword2]
        exist1_list = ['1' if x else '0' for x in exist1]
        exist2_list = ['1' if x else '0' for x in exist2]
        exist = ['1' if any(exist1) else '0', '1' if any(exist2) else '0']

    except:
        find = '*'

    keyword1.insert(0, file_num)
    keyword2.insert(0, file_num)
    exist1_list.insert(0, file_num)
    exist2_list.insert(0, file_num)

    filepath = 'analysis_' + date + '/search_' + filename  + '_會計事項_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(keyword1)

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(exist1_list)


    filepath = 'analysis_' + date + '/search_' + filename  + '_營利事業所得稅_' + date + '.csv'
    if not os.path.isfile(filepath):
        with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(keyword2)

    with open(filepath, 'a', encoding = 'big5', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(exist2_list)


    return exist
