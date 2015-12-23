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
        pass
