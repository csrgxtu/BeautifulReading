#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: BuildUserHasBook.py
# Desc: build the edge from user to book
# Date: 23/July/2016
#
# Produced By BR
from pymongo import MongoClient
import pyorient

# connect to mongodb
client = MongoClient('mongodb://linyy:rioreader@192.168.200.22:27017/bookshelf')
db = client['bookshelf']
libc = db['library']

# connect to orientdb
orientClient = pyorient.OrientDB("192.168.100.2", 2424)
orientSession = orientClient.connect( "root", "archer" )
orientClient.db_open('bookshelf', "root", "archer" )

libs = libc.find({'user_id': {'$exists': 1}, 'bid': {'$exists': 1}})
for lib in libs:
    print 'User:', lib['user_id'], 'Book:', lib['bid']
    command = 'create edge UserHasBook from (select from User where user_id=' + lib['user_id'] + ') to (select from Book where bid=' + lib['bid'] + ')'
    orientClient.command(command)

# 释放orient资源
orientClient.db_close()
