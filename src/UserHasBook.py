#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: UserHasBook.py
# Desc: 建立user到book的关系
# Date: 24/July/2016
#
# Produced By BR
from pymongo import MongoClient
import pyorient

# connect to mongodb
# client = MongoClient('mongodb://linyy:rioreader@192.168.200.22:27017/bookshelf')
client = MongoClient('mongodb://127.0.0.1:27017/bookshelf')
db = client['bookshelf']
libc = db['library']

# connect to orientdb
orientClient = pyorient.OrientDB("192.168.100.2", 2424)
orientSession = orientClient.connect( "root", "archer")
orientClient.db_open('bookshelf', "root", "archer")

# 从每条library记录中解析用户书籍关系
libs = libc.find({'user_id': {'$exists': 1}, 'bid': {'$exists': 1}}, no_cursor_timeout = True)
for lib in libs:
    try:
        cmd = 'create edge UserHasBook from (select from User where user_id="' + lib['user_id'] + '" limit 1) to (select from Book where bid="' + lib['bid'] + '" limit 1)'
        orientClient.command(cmd)
        print 'User:', lib['user_id'], 'Book:', lib['bid']
    except:
        print 'User:', lib['user_id'], 'Book:', lib['bid'], 'vertex not exist'

# 释放orient资源
libs.close()
orientClient.db_close()