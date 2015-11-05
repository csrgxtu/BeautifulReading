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

def worker(start, offset):
    cookie = 'shaishufang=Mjc5MTYwfGZmY2VmYzIyYmMxZjhlZThjNzgzYjFlOGIxOWUwODg2'
    host = "localhost"
    port = 3306
    username = 'root'
    password = 'root'
    database = 'shaishufang'

    m = MySQLDB(host, port, username, password, database)

    for i in range(start, start + offset):
        ui = UserIsbns(str(i), cookie)
        isbns = ui.run()
        userModel = {'UserID': i, 'UserName': ui.getUserName(), 'TotalBooks': ui.getTotalBooks()}
        if not m.InsertUsers(userModel):
            print 'fuck it'

        for isbn in isbns:
            bookModel = {'ISBN': isbn, 'BookName': 'Unknow', 'UserID': i}
            m.InsertBooks(bookModel)

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
    # run()
    worker(112264, 1)
