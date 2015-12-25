#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: StaticHtmlParser.py
# Date: 23/Dec/2015
# Desc: parser static html, and return the book info list
#
# Produced By BR
from bs4 import BeautifulSoup
from Utility import loadFile

class StaticHtmlParser(object):
    HTML = None
    Soup = None

    def __init__(self, filename):
        self.HTML = loadFile(filename)
        self.Soup = BeautifulSoup(self.HTML, "lxml")
        # pass

    def getBookInfos(self):
        mat = []
        for item in self.Soup.find_all('table')[-1].find('tbody').find_all('tr'):
            book = []
            for data in item.find_all('td'):
                book.append(data.getText())
            
            #print book[1], book[-2]
            #print book
            mat.append([book[1], book[-2]])

        return mat
        # pass
