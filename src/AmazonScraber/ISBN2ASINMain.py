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
from multiprocessing import Process, current_process
import sys

def run(appids, isbns):
    # print current_process().name
    i = ISBN2ASIN(appids, isbns)
    i.run(current_process().name)

if __name__ == '__main__':
    # Usage: ISBN2ASINMain.py appids.txt isbns.data coreNum
    if len(sys.argv) != 4:
        print 'Usage: ISBN2ASINMain.py appids.txt isbns.data coreNum'
        sys.exit(1)

    appids = loadIsbns(sys.argv[1])
    isbns = loadIsbns(sys.argv[2])

    jobs = []

    step = len(isbns)/int(sys.argv[3])
    for i in range(int(sys.argv[3])):
        if i == range(int(sys.argv[3]))[-1]:
            start = i * step
            end = len(isbns)
        else:
            start = i * step
            end = i * step + step
        p = Process(target=run, args=(appids, isbns[start:end], ))
        jobs.append(p)
        p.start()
