#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# Date: 22/Sep/2015
# File: BasicInfoScraper.py
# Desc: midleware between BasicInfoParser and BasicInfoScraperMain
#
# Produced By BR(BeautifulReading)
from Download import Download
from util import *
import json
from BasicInfoParser import BasicInfoParser

class BasicInfoScraper(object):
    ASINS = None

    def __init__(self, asins):
        self.ASINS = asins

    def run(self, processName='MainProcess'):
        for asin in self.ASINS:
            url = 'http://www.amazon.cn/dp/' + asin
            d = Download(url)
            if d.doRequest():
                print 'ERROR[' + processName + ']: ', asins, 'NERR'
                appendstr2file(asins, './NERRBasicInfo.txt')
                continue

            b = BasicInfoParser(d.getSOURCE())
            jsonRes = b.run()

            if json.loads(jsonRes):
                print 'info[' + processName + ']: ', asins
                appendstr2file(jsonRes, './OKBasicInfo.txt')
            else:
                print 'WARN[' + processName + ']: ', asins, 'NOER'
                appendstr2file(asins, './NOERBasicInfo.txt')
