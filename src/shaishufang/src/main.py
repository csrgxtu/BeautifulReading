#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 28/Oct/2015
# File: main.py
# Desc: main File
#
# Produced By CSRGXTU
from UserIsbns import UserIsbns
from Utility import appendlst2file

def run():
    uid = '90661'
    cookie = 'shaishufang=Mjc5MTYwfGZmY2VmYzIyYmMxZjhlZThjNzgzYjFlOGIxOWUwODg2'

    for i in range(1, 279653):
        ui = UserIsbns(str(i), cookie)
        isbns = ui.run()
        appendlst2file(isbns, 'isbns.txt')

if __name__ == '__main__':
    run()
