#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 28/Oct/2015
# File: main.py
# Desc: main File
#
# Produced By CSRGXTU
from UserIsbns import UserIsbns
from Utility import saveLstToFile

def run():
    uid = '90661'
    cookie = 'shaishufang=Mjc5MTYwfGZmY2VmYzIyYmMxZjhlZThjNzgzYjFlOGIxOWUwODg2'

    ui = UserIsbns(uid, cookie)
    isbns = ui.run()
    saveLstToFile('isbns.txt', isbns)

if __name__ == '__main__':
    run()
