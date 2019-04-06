import csv
import re
date = '20180101_20181231'

catalog = []
with open('catalog_' + date + '.csv', newline='\n') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        catalog.append(row)

total = catalog[-1][0]

with open('value_' + date + '.csv', 'w', encoding = 'big5', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['案件區分', '辯論終結日期', '原告', '原告代表人', '原告訴訟代理人', '被告', '被告代表人', '被告訴訟代理人', '不服訴願日期', '判決結果', '判決日期', '第幾庭', '審判長及法官'])
    for f_num in range(int(total)):
        verdict_type = ''
        end_date = ''
        plaintiff = ''
        defendant = ''
        plain_attorney = ''
        defend_attorney = ''
        plain_represent = ''
        defend_represent = ''
        unsatisfied_date = ''
        result = ''
        judgment_date = ''
        court_num = ''
        judge = ''

        file = open('data_' + date + '/' + str(f_num + 1) + '.txt', 'r', encoding = 'utf8')
        verdict = file.read().replace('　', '').replace(' ', '').replace('\ue4fd', ' ').replace('再審', '').replace('\ue3f1', '').replace('\u6052', '?')
        type_line = verdict[:200]
        set_line = verdict[:verdict.index('上列當事人')]
        unsatisfied_date = verdict[verdict.index('中華民國') + 4: verdict.index('日', verdict.index('中華民國')) + 1].replace('\n', '')
        if type_line.find('簡上') == -1:
            verdict_type = '訴(更)'
            set_line = set_line.replace('\n', '').replace('原告', '#').replace('被告', '#').split('#')
            end_date = set_line[0][set_line[0].index('號', len(set_line[0]) - 15) + 1: -4]

            # print(unsatisfied_date)
            # print(type_line)
            #原告
            plaintiff_line = set_line[1]
            if set_line[1].find('代表人') != -1:
                plaintiff_line = plaintiff_line.replace('代表人', ' #')
            if set_line[1].find('訴訟代理人') != -1:
                plaintiff_line = plaintiff_line.replace('訴訟代理人', ' @')
            plaintiff_line = plaintiff_line.split(' ')
            for num in range(len(plaintiff_line)):
                if num == 0:
                    plaintiff = plaintiff_line[num]
                elif plaintiff_line[num][0] == '#':
                    plain_represent += plaintiff_line[num][1:]
                elif plaintiff_line[num][0] == '@':
                    plain_attorney += plaintiff_line[num][1:]
                else:
                    print(plaintiff_line[num])

            #被告
            defend_line = set_line[2]
            if set_line[2].find('代表人') != -1:
                defend_line = defend_line.replace('代表人', '$#')
            if set_line[2].find('訴訟代理人') != -1:
                defend_line = defend_line.replace('訴訟代理人', '$@')
            defend_line = defend_line.split('$')
            for num in range(len(defend_line)):
                if num == 0:
                    defendant = defend_line[num]
                elif defend_line[num][0] == '#':
                    defend_represent += defend_line[num][1:]
                elif defend_line[num][0] == '@':
                    defend_attorney += defend_line[num][1:]
                else:
                    print(defend_line[num])

            '''
            plain_represent = plain_represent[:-1]
            plain_attorney = plain_attorney[:-1]
            '''
            '''
            print('原告: ' + plaintiff)
            print('原告代表人: ' + plain_represent)
            print('原告訴訟代理人: ' + plain_attorney)
            print('被告: ' + defendant)
            print('被告代表人: ' + defend_represent)
            print('被告訴訟代理人: ' + defend_attorney)
            print('不服訴願日期: ' + unsatisfied_date)
            '''

        if type_line.find('簡上') != -1:
            verdict_type = '簡上'
            set_line = set_line.replace('\n', '').replace('被上訴人', '#').replace('上訴人', '#').split('#')
            #unsatisfied_date = verdict[verdict.index('中華民國') + 4: verdict.index('日', verdict.index('中華民國')) + 1].replace('\n', '')
            # print(type_line)
            #原告
            plaintiff_line = set_line[1]
            if set_line[1].find('代表人') != -1:
                plaintiff_line = plaintiff_line.replace('代表人', '$#')
            if set_line[1].find('訴訟代理人') != -1:
                plaintiff_line = plaintiff_line.replace('訴訟代理人', '$@')
            plaintiff_line = plaintiff_line.split('$')
            for num in range(len(plaintiff_line)):
                if num == 0:
                    plaintiff = plaintiff_line[num]
                elif plaintiff_line[num][0] == '#':
                    plain_represent += plaintiff_line[num][1:]
                elif plaintiff_line[num][0] == '@':
                    plain_attorney += plaintiff_line[num][1:]
                else:
                    print(plaintiff_line[num])

            #被告
            defend_line = set_line[2]
            if set_line[2].find('代表人') != -1:
                defend_line = defend_line.replace('代表人', '$#')
            if set_line[2].find('訴訟代理人') != -1:
                defend_line = defend_line.replace('訴訟代理人', '$@')
            defend_line = defend_line.split('$')
            for num in range(len(defend_line)):
                if num == 0:
                    defendant = defend_line[num]
                elif defend_line[num][0] == '#':
                    defend_represent += defend_line[num][1:]
                elif defend_line[num][0] == '@':
                    defend_attorney += defend_line[num][1:]
                else:
                    print(defend_line[num])
            '''
            plain_represent = plain_represent[:-1]
            plain_attorney = plain_attorney[:-1]
            defend_represent = defend_represent[:-1]
            defend_attorney = defend_attorney[:-1]
            '''
        '''
            print('上訴人: ' + plaintiff)
            print('上訴人代表人: ' + plain_represent)
            print('上訴人訴訟代理人: ' + plain_attorney)
            print('被上訴人: ' + defendant)
            print('被上訴人代表人: ' + defend_represent)
            print('被上訴人訴訟代理人: ' + defend_attorney)
            print('不服訴願日期: ' + unsatisfied_date)
        '''
        # result
        result_line = verdict[verdict.index('主文'): verdict.index('。', verdict.index('主文'))].replace('\n', '')
        if result_line.find('駁回') != -1:
            result = '駁回'
        elif result_line.find('撤銷') != -1:
            result = '撤銷'
        elif result_line.find('廢棄') != -1:
            result = '廢棄'
        else:
            result = '????'
            print(result_line)
        end_index = verdict.index('中華民國', len(verdict) - 1200)
        result_line = verdict[end_index: end_index + 50].split('\n')
        for line in result_line:
            if line.find('中華民國') != -1:
                judgment_date = line[4:]
            elif line.find('臺北高等行政法院') != -1:
                court_num = line[-2]
            elif line.find('法官') != -1:
                judge += line[line.index('法官') + 2:] + '、'
        judge = judge[:-1]

        '''
        print(num)
        print(result_line)
        print('判決日期: ' + judgment_date)
        print('台北高等行政法院第幾庭: ' + court_num)
        print('審判長及法官: ' + judge)
        '''

        output = [verdict_type, end_date, plaintiff, plain_represent, plain_attorney, defendant, defend_represent, defend_attorney, unsatisfied_date, result, judgment_date, court_num, judge]
        #output = [verdict_type.encode('big5'), end_date.encode('big5'), plaintiff.encode('big5'), plain_represent.encode('big5'), plain_attorney.encode('big5'), defendant.encode('big5'), defend_represent.encode('big5'), defend_attorney.encode('big5'), unsatisfied_date.encode('big5'), result.encode('big5'), judgment_date.encode('big5'), court_num.encode('big5'), judge.encode('big5')]
        writer.writerow(output)
