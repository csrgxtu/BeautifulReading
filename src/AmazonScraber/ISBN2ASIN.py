#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 21/Sep/2015
# File: ISBN2ASIN.py
# Desc: use amazon.cn search service turn ISBN to ASIN
#
# Produced By BR(BeautifulReading)
from Download import Download
from Util import *
from itertools import cycle

class ISBN2ASIN(object):
    APPIDS = None
    ISBNS = None
    APPIDS_CYCLE = None
    # http://csrgxtua-01.appspot.com/url?url=http://www.amazon.cn/s/ref=nb_sb_noss?__mk_zh_CN=亚马逊网站&field-keywords=

    def __init__(self, appids, isbns):
        self.APPIDS = appids
        self.ISBNS = isbns
        self.APPIDS_CYCLE = cycle(self.APPIDS)

    def run(self):
        for isbn in ISBNS:
            url = 'http://' + self.APPIDS_CYCLE.next() + '.appsport.com/url?url=http://www.amazon.cn/s/ref=nb_sb_noss?__mk_zh_CN=亚马逊网站&field-keywords='
            print url
