#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 28/Oct/2015
# File: main.py
# Desc: main File
#
# Produced By CSRGXTU
import multiprocessing

from UserIsbns import UserIsbns
from Utility import appendlst2file

def worker(start, offset):
    cookie = 'shaishufang=Mjc5MTYwfGZmY2VmYzIyYmMxZjhlZThjNzgzYjFlOGIxOWUwODg2'

    for i in range(start, start + offset):
        ui = UserIsbns(str(i), cookie)
        isbns = ui.run()
        appendlst2file(isbns, 'isbns.txt')

def run():
    jobs = []

    index = 1
    for i in range(50):
        p = multiprocessing.Process(target=worker, args=(index, 5593))
        jobs.append(p)
        p.start()
        index = index + 5593

if __name__ == '__main__':
    run()
