#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Archer Reilly
# File: 1000books.py
# Date: 13/Sep/2015
# Desc: get price and availablity for 1000 books
#
# Produced By BR(BeautifulReading)
from util import ldUserAgents, loadMatrixFromFile, appendstr2file
from BookAPI import BookAPI
from random import choice
from time import sleep
import json

def run():
    user_agents = ldUserAgents('./UserAgentString.json')
    bookinfos = loadMatrixFromFile('./kaijuan.csv')
    newbookinfos = []
    sellers = ['亚马逊', '京东', '当当', '北发', '淘书', '博库', '文轩', '中国图书', 'China-pub']

    for index in range(1, len(bookinfos)):
        print 'INFO: processing', bookinfos[index][0],

        b = BookAPI(bookinfos[index][0], choice(user_agents))
        JsonData = json.loads(b.api())
        if JsonData['error']:
            appendstr2file(JsonData['isbn'], 'error.log')
            print 'ERROR: got an network error '
            sleep(1)
            continue

        tmpLst = bookinfos[index]

        if JsonData['total'] == 0:
            for seller in sellers:
                tmpLst.append('None')
            print 'WARNING: no data'
            sleep(1)
            continue

        for seller in sellers:
            tmpLst.append('None')
            for key in JsonData['data']:
                if seller.decode('UTF-8') in key:
                    del tmpLst[-1]
                    tmpLst.append(JsonData['data'][key])
                    break
        newbookinfos.append(tmpLst)

        print 'Done'
        sleep(1)

    saveMatrixToFile('newkaijuan.csv', newbookinfos)

if __name__ == "__main__":
    run()
