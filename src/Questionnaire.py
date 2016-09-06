#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer
# File: Questionnaire.py
# Desc: 从调查问卷的csv文件中统计一些数据
# Date: 05/Sep/2015
import csv
import sys

QuestionnaireMat = []
csvFile = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(csvFile)
    for row in reader:
        QuestionnaireMat.append(row)

    print 'CSV 2 Matrix: ok'
finally:
    csvFile.close()

# 同意，反对，强烈同意，强烈反对
# AllInOne = []
# for row in QuestionnaireMat[1:]:
#     AllInOne.extend(row[3:-4])

# questions
Questions = QuestionnaireMat[0][3:-4]

# 按照学历统计
Degree = []
for row in QuestionnaireMat[1:]:
    Degree.append(row[-1])
Degree = list(set(Degree))

print '\n按照学历进行统计:'
DegreeCsv = open('./degree.csv', 'wt')
writer = csv.writer(DegreeCsv)
writer.writerow(('学历', '问题', '同意', '反对', '强烈同意', '强烈反对'))
for d in Degree:
    for q in range(len(Questions)):
        aIndex = 0
        bIndex = 0
        cIndex = 0
        dIndex = 0
        for row in QuestionnaireMat[1:]:
            if row[-1] != d:
                continue

            if row[3 + q] == '同意':
                aIndex = aIndex + 1
            elif row[3 + q] == '反对':
                bIndex = bIndex + 1
            elif row[3 + q] == '强烈同意':
                cIndex = cIndex + 1
            elif row[3 + q] == '强烈反对':
                dIndex = dIndex + 1

        print d, Questions[q], aIndex, bIndex, cIndex, dIndex
        writer.writerow((d, Questions[q], aIndex, bIndex, cIndex, dIndex))

DegreeCsv.close()


# 按照性别统计
Sex = []
for row in QuestionnaireMat[1:]:
    Sex.append(row[-4])
Sex = list(set(Sex))

print '\n按照性别统计:'
SexCsv = open('./sex.csv', 'wt')
writer = csv.writer(SexCsv)
writer.writerow(('性别', '问题', '同意', '反对', '强烈同意', '强烈反对'))
for s in Sex:
    for q in range(len(Questions)):
        aIndex = 0
        bIndex = 0
        cIndex = 0
        dIndex = 0
        for row in QuestionnaireMat[1:]:
            if row[-1] != d:
                continue

            if row[3 + q] == '同意':
                aIndex = aIndex + 1
            elif row[3 + q] == '反对':
                bIndex = bIndex + 1
            elif row[3 + q] == '强烈同意':
                cIndex = cIndex + 1
            elif row[3 + q] == '强烈反对':
                dIndex = dIndex + 1

        print s, Questions[q], aIndex, bIndex, cIndex, dIndex
        writer.writerow((s, Questions[q], aIndex, bIndex, cIndex, dIndex))

SexCsv.close()

# # 按照年收入
Wage = []
for row in QuestionnaireMat[1:]:
    Wage.append(row[-2])
Wage = list(set(Wage))

print '\n按照工资统计:'
WageCsv = open('./wage.csv', 'wt')
writer = csv.writer(WageCsv)
writer.writerow(('年收入', '问题', '同意', '反对', '强烈同意', '强烈反对'))
for w in Wage:
    for q in range(len(Questions)):
        aIndex = 0
        bIndex = 0
        cIndex = 0
        dIndex = 0
        for row in QuestionnaireMat[1:]:
            if row[-2] != w:
                continue

            if row[3 + q] == '同意':
                aIndex = aIndex + 1
            elif row[3 + q] == '反对':
                bIndex = bIndex + 1
            elif row[3 + q] == '强烈同意':
                cIndex = cIndex + 1
            elif row[3 + q] == '强烈反对':
                dIndex = dIndex + 1

        print w, Questions[q], aIndex, bIndex, cIndex, dIndex
        writer.writerow((w, Questions[q], aIndex, bIndex, cIndex, dIndex))

WageCsv.close()

#
# # 按照出生年份
Year = []
for row in QuestionnaireMat[1:]:
    Year.append(row[-3])
Year = list(set(Year))

print '\n按照年份统计:'
YearCsv = open('./year.csv', 'wt')
writer = csv.writer(YearCsv)
writer.writerow(('出生年份', '问题', '同意', '反对', '强烈同意', '强烈反对'))
for y in Year:
    for q in range(len(Questions)):
        aIndex = 0
        bIndex = 0
        cIndex = 0
        dIndex = 0
        for row in QuestionnaireMat[1:]:
            if row[-3] != y:
                continue

            if row[3 + q] == '同意':
                aIndex = aIndex + 1
            elif row[3 + q] == '反对':
                bIndex = bIndex + 1
            elif row[3 + q] == '强烈同意':
                cIndex = cIndex + 1
            elif row[3 + q] == '强烈反对':
                dIndex = dIndex + 1

        print y, Questions[q], aIndex, bIndex, cIndex, dIndex
        writer.writerow((y, Questions[q], aIndex, bIndex, cIndex, dIndex))

YearCsv.close()
