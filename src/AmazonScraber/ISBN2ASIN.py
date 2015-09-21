#!/usr/bin/env python
# coding=utf-8
# Author: Archer Reilly
# Date: 21/Sep/2015
# File: ISBN2ASIN.py
# Desc: use amazon.cn search service turn ISBN to ASIN
#
# Produced By BR(BeautifulReading)
from Download import Download
from util import *
from itertools import cycle
import json
from time import sleep
from ASINParser import ASINParser

class ISBN2ASIN(object):
    APPIDS = None
    ISBNS = None
    APPIDS_CYCLE = None

    def __init__(self, appids, isbns):
        self.APPIDS = appids
        self.ISBNS = isbns
        self.APPIDS_CYCLE = cycle(self.APPIDS)

    def run(self):
        for isbn in self.ISBNS:
            url = 'http://www.amazon.cn/s/ref=nb_sb_noss?field-keywords=' + isbn
            d = Download(url)
            if d.doRequest():
                print 'ERROR: ', isbn, 'NERR'
                continue

            asin = ASINParser(d.getSOURCE())
            if asin.getAsin():
                print 'INFO: ', isbn, asin.getAsin()
            else:
                print 'WARN: ', isbn, 'NOER'
