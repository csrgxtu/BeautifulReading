#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 28/Oct/2015
# File: main.py
# Desc: main File
#
# Produced By CSRGXTU
from UserIsbns import UserIsbns

def run():
    uid = '258536'
    cookie = 'shaishufang=Mjc5MTYwfGZmY2VmYzIyYmMxZjhlZThjNzgzYjFlOGIxOWUwODg2'

    ui = UserIsbns(uid, cookie)
    print ui.run()

if __name__ == '__main__':
    run()
