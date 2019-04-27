#!/usr/bin/env python
# coding: utf-8

import csv
import re
import os

from processorlib.debate_end_simple import get_debate_end_simple
from processorlib.plaintiff_simple import get_plaintiff_simple
from processorlib.plain_represent_simple import get_plain_represent_simple
from processorlib.plain_attorney_simple import get_plain_attorney_simple
from processorlib.defendant_simple import get_defendant_simple
from processorlib.defend_represent_simple import get_defend_represent_simple
from processorlib.defend_attorney_simple import get_defend_attorney_simple
from processorlib.plaintiff_litigation import get_plaintiff_litigation
from processorlib.plain_represent_litigation import get_plain_represent_litigation
from processorlib.plain_attorney_litigation import get_plain_attorney_litigation
from processorlib.defendant_litigation import get_defendant_litigation
from processorlib.defend_represent_litigation import get_defend_represent_litigation
from processorlib.defend_attorney_litigation import get_defend_attorney_litigation
from processorlib.unsatisfied_date import get_unsatisfied_date
from processorlib.unsatisfied_reason import get_unsatisfied_reason
from processorlib.verdict_result import get_verdict_result
from processorlib.verdict_date import get_verdict_date
from processorlib.court_num import get_court_num
from processorlib.judge import get_judge
from processorlib.reason_content_simple import get_reason_content_simple
from processorlib.reason_content_again import get_reason_content_again
from processorlib.reason_content_litigation import get_reason_content_litigation

from processorlib.result_content import get_result_content
from processorlib.search_keyword import search_keyword
from processorlib.money_inquiry import get_money_inquiry
from processorlib.plain_content_simple import get_plain_content_simple
from processorlib.plain_content_litigation import get_plain_content_litigation
from processorlib.defend_content_simple import get_defend_content_simple
from processorlib.defend_content_litigation import get_defend_content_litigation
from processorlib.special_result import get_special_result


date = '1060101_1061231'

if __name__ == '__main__':
    catalog = []
    with open('catalog_' + date + '.csv', newline='\n') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            catalog.append(row)
    total = catalog[-1][0]

    if not os.path.isdir('analysis_' + date):
        os.mkdir('analysis_' + date)

    with open('value_' + date + '.csv', 'w', encoding = 'big5', newline='\n') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['案件編號', '辯論終結日期', '原告', '原告代表人', '原告訴訟代理人', '被告', '被告代表人', '被告訴訟代理人', '不服訴願日期', '判決結果', '判決日期', '第幾庭', '審判長及法官', '事實字數', '原告字數', '被告字數', '判斷字數', '原告搜尋結果', '被告搜尋結果', '判斷搜尋結果', '補徵稅額', '自為判決'])

        for f_num in range(int(total)):
            file = open('data_' + date + '/' + str(f_num + 1) + '.txt', 'r', encoding = 'utf8')
            verdict = file.read().replace('　', '').replace(' ', '').replace('\ue4fd', ' ').replace('\ue3f1', '').replace('\u6052', '?').replace('\ue481', '?').replace('\ue4da', '?').replace('\u5afa', '?').replace('再審', '')
            end_date = ''
            type_line = verdict[:100].replace('再審', '')

            if type_line.find('訴字') != -1 or type_line.find('訴更') != -1:
                end_date = get_debate_end_simple(verdict, date, f_num + 1)
                reason_content, reason_content_num = get_reason_content_simple(verdict, date, f_num + 1)
                plain_content, plain_content_num = get_plain_content_simple(verdict, date, f_num + 1)
                defend_content, defend_content_num = get_defend_content_simple(verdict, date, f_num + 1)
                plaintiff = get_plaintiff_simple(verdict, date, f_num + 1)
                plain_represent = get_plain_represent_simple(verdict, date, f_num + 1)
                plain_attorney = get_plain_attorney_simple(verdict, date, f_num + 1)
                defendant = get_defendant_simple(verdict, date, f_num + 1)
                defend_represent = get_defend_represent_simple(verdict, date, f_num + 1)
                defend_attorney = get_defend_attorney_simple(verdict, date, f_num + 1)

            elif type_line.find('再字') != -1:
                reason_content, reason_content_num = get_reason_content_again(verdict, date, f_num + 1)
                #plain_content = get_plain_content_again(verdict, date, f_num + 1)
                plain_content, plain_content_num = get_plain_content_simple(verdict, date, f_num + 1)
                defend_content, defend_content_num = get_defend_content_simple(verdict, date, f_num + 1)
                plaintiff = get_plaintiff_simple(verdict, date, f_num + 1)
                plain_represent = get_plain_represent_simple(verdict, date, f_num + 1)
                plain_attorney = get_plain_attorney_simple(verdict, date, f_num + 1)
                defendant = get_defendant_simple(verdict, date, f_num + 1)
                defend_represent = get_defend_represent_simple(verdict, date, f_num + 1)
                defend_attorney = get_defend_attorney_simple(verdict, date, f_num + 1)

            elif type_line.find('簡上') != -1:
                reason_content, reason_content_num = get_reason_content_litigation(verdict, date, f_num + 1)
                plain_content, plain_content_num = get_plain_content_litigation(verdict, date, f_num + 1)
                defend_content, defend_content_num = get_defend_content_litigation(verdict, date, f_num + 1)
                plaintiff = get_plaintiff_litigation(verdict, date, f_num + 1)
                plain_represent = get_plain_represent_litigation(verdict, date, f_num + 1)
                plain_attorney = get_plain_attorney_litigation(verdict, date, f_num + 1)
                defendant = get_defendant_litigation(verdict, date, f_num + 1)
                defend_represent = get_defend_represent_litigation(verdict, date, f_num + 1)
                defend_attorne = get_defend_attorney_litigation(verdict, date, f_num + 1)


            result_content, result_content_num = get_result_content(verdict, date, f_num + 1)

            plain_search = search_keyword(plain_content, '納稅者權利保護法', date, f_num + 1, 'plain_content_納稅者權利保護法')
            defend_search = search_keyword(defend_content, '納稅者權利保護法', date, f_num + 1, 'defend_content_納稅者權利保護法')
            result_search = search_keyword(result_content, '納稅者權利保護法', date, f_num + 1, 'result_content_納稅者權利保護法')

            special_result =  get_special_result(verdict, date, f_num + 1)
            unsatisfied_date =  get_unsatisfied_date(verdict, date, f_num + 1)
            unsatisfied_reason =  get_unsatisfied_reason(verdict, date, f_num + 1)
            result = get_verdict_result(verdict, date, f_num + 1)
            judgment_date = get_verdict_date(verdict, date, f_num + 1)
            court_num = get_court_num(verdict, date, f_num + 1)
            judge = get_judge(verdict, date, f_num + 1)
            money_inquiry = get_money_inquiry(reason_content, date, f_num + 1)


            output = [f_num + 1, end_date, plaintiff, plain_represent, plain_attorney, defendant, defend_represent, defend_attorney, unsatisfied_date, result, judgment_date, court_num, judge, reason_content_num, plain_content_num, defend_content_num, result_content_num, plain_search, defend_search, result_search, money_inquiry, special_result]
            writer.writerow(output)

    input('Success!! Please press any key to continue...')
