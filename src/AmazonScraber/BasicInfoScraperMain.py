#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# Date: 22/Sep/2015
# File: BasicInfoScraperMain.py
# Desc: scrab the basic info from book page according to the
# ASINs
#
# Produced By BR(BeautifulReading)
from util import *
import sys
from multiprocessing import Process, current_process
from BasicInfoScraper import BasicInfoScraper

def run(appids, asins):
    # print current_process().name
    i = BasicInfoScraper(asins)
    i.run(current_process().name)


if __name__ == '__main__':
    # Usage: BasicInfoScraperMain.py appids.txt asins.data coreNum
    if len(sys.argv) != 3:
        print 'Usage: BasicInfoScraperMain.py asins.data coreNum'
        sys.exit(1)

    asins = loadIsbns(sys.argv[1])

    jobs = []

    step = len(asins)/int(sys.argv[2])
    for i in range(int(sys.argv[2])):
        if i == range(int(sys.argv[2]))[-1]:
            start = i * step
            end = len(asins)
        else:
            start = i * step
            end = i * step + step
        p = Process(target=run, args=(asins[start:end], ))
        jobs.append(p)
        p.start()
