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
from processorlib.search_keyword_num import search_keyword_num
from processorlib.money_inquiry import get_money_inquiry
from processorlib.penalty_inquiry import get_penalty_inquiry
from processorlib.plain_content_simple import get_plain_content_simple
from processorlib.plain_content_litigation import get_plain_content_litigation
from processorlib.defend_content_simple import get_defend_content_simple
from processorlib.defend_content_litigation import get_defend_content_litigation
from processorlib.special_result import get_special_result
from processorlib.total_content import get_total_content
from processorlib.issue_content import get_issue_content
from processorlib.special_keyword import search_special_keyword

start = input("start(yyymmdd): ")
end = input("end(yyymmdd): ")
date = start + '_' + end
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
        writer.writerow(['案件編號', '案件類型', '辯論終結年', '辯論終結月', '辯論終結日', '原告', '原告代表人', '原告訴訟代理人', '被告', '被告代表人', '被告訴訟代理人', '不服訴願年', '不服訴願月', '不服訴願日', '撤銷', '駁回', '廢棄', '訴訟費用', '判決年', '判決月', '判決日', '第幾庭', '審判長及法官', '事實字數', '原告字數', '被告字數', '爭點字數', '判斷字數', '總字數', '原告搜尋納保法', '被告搜尋納保法', '判斷搜尋納保法', '原告搜尋稅捐稽徵法', '被告搜尋稅捐稽徵法', '判斷搜尋稅捐稽徵法', '判斷搜尋會計事項', '判斷搜尋營利事業所得稅', '原告搜尋會計事項', '原告搜尋營利事業所得稅', '被告搜尋會計事項', '被告搜尋營利事業所得稅', '判斷搜尋會計事項', '判斷搜尋營利事業所得稅', '罰鍰次數','補徵稅額金額', '所漏稅額金額',  '罰鍰金額', '判決主文'])

        for f_num in range(int(total)):
            file = open('data_' + date + '/' + str(f_num + 1) + '.txt', 'r', encoding = 'utf8')
            content_verdict = file.read().replace('　', '').replace('再審', '')
            verdict = content_verdict.replace(' ', '')
            #.replace('\ue4fd', ' ').replace('\ue3f1', '').replace('\u6052', '?').replace('\ue481', '?').replace('\ue4da', '?').replace('\u5afa', '?')
            end_date = ['', '', '']
            type_line = verdict[:100].replace('再審', '')
            if type_line.find('訴字') != -1:
                verdict_type = '訴'
            if type_line.find('訴更') != -1:
                verdict_type = '訴更'
            if type_line.find('訴字') != -1 or type_line.find('訴更') != -1:
                end_date = get_debate_end_simple(verdict, date, f_num + 1)
                plaintiff = get_plaintiff_simple(verdict, date, f_num + 1)
                plain_represent = get_plain_represent_simple(verdict, date, f_num + 1)
                plain_attorney = get_plain_attorney_simple(verdict, date, f_num + 1)
                defendant = get_defendant_simple(verdict, date, f_num + 1)
                defend_represent = get_defend_represent_simple(verdict, date, f_num + 1)
                defend_attorney = get_defend_attorney_simple(verdict, date, f_num + 1)

            elif type_line.find('再字') != -1:
                verdict_type = '再'
                plaintiff = get_plaintiff_simple(verdict, date, f_num + 1)
                plain_represent = get_plain_represent_simple(verdict, date, f_num + 1)
                plain_attorney = get_plain_attorney_simple(verdict, date, f_num + 1)
                defendant = get_defendant_simple(verdict, date, f_num + 1)
                defend_represent = get_defend_represent_simple(verdict, date, f_num + 1)
                defend_attorney = get_defend_attorney_simple(verdict, date, f_num + 1)

            elif type_line.find('簡上') != -1:
                verdict_type = '簡上'
                plaintiff = get_plaintiff_litigation(verdict, date, f_num + 1)
                plain_represent = get_plain_represent_litigation(verdict, date, f_num + 1)
                plain_attorney = get_plain_attorney_litigation(verdict, date, f_num + 1)
                defendant = get_defendant_litigation(verdict, date, f_num + 1)
                defend_represent = get_defend_represent_litigation(verdict, date, f_num + 1)
                defend_attorney = get_defend_attorney_litigation(verdict, date, f_num + 1)

            reason_content, reason_content_num = get_reason_content_simple(verdict, date, f_num + 1)
            plain_content, plain_content_num = get_plain_content_simple(content_verdict, date, f_num + 1)
            defend_content, defend_content_num = get_defend_content_simple(content_verdict, date, f_num + 1)
            issue_content, issue_content_num, issue_end = get_issue_content(verdict, date, f_num + 1)
            result_content, result_content_num = get_result_content(content_verdict, date, f_num + 1, issue_end)
            total_content_num = get_total_content(verdict, date, f_num + 1)
            plain_search_1 = search_keyword(plain_content, '納.*保.*法第.*條第.*項、?', date, f_num + 1, 'plain_content_納稅者權利保護法', 1)
            defend_search_1 = search_keyword(defend_content, '納.*保.*法第.*條第.*項、?', date, f_num + 1, 'defend_content_納稅者權利保護法', 1)
            result_search_1 = search_keyword(result_content, '納.*保.*法第.*條第.*項、?', date, f_num + 1, 'result_content_納稅者權利保護法', 1)

            plain_search_2 = search_keyword(plain_content, '稅捐稽徵法第(?:[11十一]{2}條?之[3-7三四五六七]{1}條?|[12十二]{2}條?之[1一]{1}條?)', date, f_num + 1, 'plain_content_稅捐稽徵法', 2)
            defend_search_2 = search_keyword(defend_content, '稅捐稽徵法第(?:[11十一]{2}條?之[3-7三四五六七]{1}條?|[12十二]{2}條?之[1一]{1}條?)', date, f_num + 1, 'defend_content_稅捐稽徵法', 2)
            result_search_2 = search_keyword(result_content, '稅捐稽徵法第(?:[11十一]{2}條?之[3-7三四五六七]{1}條?|[12十二]{2}條?之[1一]{1}條?)', date, f_num + 1, 'result_content_稅捐稽徵法', 2)
            reason_search = search_keyword_num(reason_content, '罰鍰', date, f_num + 1, 'reason_content_罰鍰')
            plain_special_exist = search_special_keyword(verdict, date, f_num + 1, 'plain_content_')
            defend_special_exist = search_special_keyword(verdict, date, f_num + 1, 'defend_content_')
            result_special_exist = search_special_keyword(verdict, date, f_num + 1, 'result_content_')
            reason_special_exist = search_special_keyword(verdict, date, f_num + 1, 'reason_content_')

            #special_result =  get_special_result(verdict, date, f_num + 1)
            unsatisfied_date =  get_unsatisfied_date(verdict, date, f_num + 1)
            unsatisfied_reason =  get_unsatisfied_reason(verdict, date, f_num + 1)
            result, maintext = get_verdict_result(verdict, date, f_num + 1)
            judgment_date = get_verdict_date(verdict, date, f_num + 1)
            court_num = get_court_num(verdict, date, f_num + 1)
            judge = get_judge(verdict, date, f_num + 1)
            money_inquiry, leak_money_inquiry = get_money_inquiry(reason_content, date, f_num + 1)
            penalty_inquiry = get_penalty_inquiry(reason_content, date, f_num + 1)
            output = [f_num + 1, verdict_type, end_date[0], end_date[1], end_date[2], plaintiff, plain_represent, plain_attorney, defendant, defend_represent, defend_attorney, unsatisfied_date[0], unsatisfied_date[1], unsatisfied_date[2], result[0], result[1], result[2], result[3], judgment_date[0], judgment_date[1], judgment_date[2] ,court_num, judge, reason_content_num, plain_content_num, defend_content_num, issue_content_num, result_content_num, total_content_num, plain_search_1, defend_search_1, result_search_1, plain_search_2, defend_search_2, result_search_2,  plain_special_exist[0], plain_special_exist[1], defend_special_exist[0], defend_special_exist[1], result_special_exist[0], result_special_exist[1], reason_special_exist[0], reason_special_exist[1], reason_search, money_inquiry, leak_money_inquiry, penalty_inquiry, maintext]
            writer.writerow(output)

    input('Success!! Please press any key to continue...')
