#!/usr/bin/env python
# coding=utf-8
# Author: Archer Reilly
# File: GetBookInfos.py
# Desc: get books information from the static html files, esp kaijuan
# Date: 23/Dec/2015
#
# Produced By BR
from Utility import appendMatrixToFileUtf
from StaticHtmlParser import StaticHtmlParser

for i in range(1, 485):
    print "Processing: ", i
    s = StaticHtmlParser('/home/archer/Downloads/htmls/' + str(i) + '.html')
    mat = s.getBookInfos()

    #print mat
    appendMatrixToFileUtf('./data.csv', mat)
