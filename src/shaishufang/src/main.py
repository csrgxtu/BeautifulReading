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
from MySQLDB import MySQLDB
from Utility import appendMatrixToFile
from ProxyDownload import ProxyDownload
import json
import time

def updateProxy(start, offset):
    url = 'http://svip.kuaidaili.com/api/getproxy/?orderid=983980639044193&num=5&browser=1&protocol=1&method=1&sp1=1&quality=0&sort=0&format=json&sep=1'
    host = "127.0.0.1"
    port = 3306
    username = 'root'
    password = 'root'
    database = 'shaishufang'
    m = MySQLDB(host, port, username, password, database)
    proxyDownload = ProxyDownload(url)
    while True:
        proxyDownload.doRequest()
        parsed_json = json.loads(proxyDownload.getSOURCE())
        tmpLst = []
        for item in parsed_json['data']['proxy_list']:
            tmpLst.append(str(item))
        m.InsertProxies(tmpLst)
        time.sleep(300)

def worker(start, offset):
    cookie = 'shaishufang=Mjc5MTYwfGZmY2VmYzIyYmMxZjhlZThjNzgzYjFlOGIxOWUwODg2'
    host = "127.0.0.1"
    port = 3306
    username = 'root'
    password = 'root'
    database = 'shaishufang'

    m = MySQLDB(host, port, username, password, database)

    for i in range(start, start + offset):
        print 'INFO[UserID]: ', i, 'Processing...'
        proxy = m.ReadProxy()
        ui = UserIsbns(str(i), cookie, proxy)
        isbns = ui.run()
        if len(isbns) == ui.getTotalBooks():
            state = 1
        else:
            state = 0

        userModel = {'UserID': i, 'UserName': ui.getUserName(), 'TotalBooks': ui.getTotalBooks(), 'State': state}
        if m.InsertUsers(userModel):
            print 'INFO[Inserted Users]: ', userModel

        for isbn in isbns:
            bookModel = {'ISBN': isbn, 'BookName': 'Unknow', 'UserID': i}
            if m.InsertBooks(bookModel):
                print 'INFO[Inserted Books]: ', bookModel

    m.CloseDB()


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
    # worker(1, 279652)
