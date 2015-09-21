#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# Date: 21/Sep/2015
# File: ISBN2ASINMain.py
# Desc: main
#
# Produced By BR(BeautifulReading)
from ISBN2ASIN import ISBN2ASIN
from util import *

if __name__ == '__main__':
    appids = loadIsbns('appids.txt')
    isbns = loadIsbns('isbns.data')
    i = ISBN2ASIN(appids, isbns)
    i.run()
