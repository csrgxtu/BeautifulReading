#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: TransforBook.py
# Desc: 将mongo里面的bookful转到orientdb里面去
# Date: 23/July/2016
#
# Produced By BR
from pymongo import MongoClient
import pyorient

# connect to mongodb
client = MongoClient('mongodb://linyy:rioreader@192.168.200.22:27017/bookshelf')
db = client['bookshelf']
bc = db['bookful']

# connect to orientdb
orientClient = pyorient.OrientDB("192.168.100.2", 2424)
orientSession = orientClient.connect( "root", "archer" )
orientClient.db_open('bookshelf', "root", "archer" )


books = bc.find({'bid': {'$exists': 1}, 'title': {'$exists': 1}})
for book in books:
    cmd = 'select from Book where bid="' + book['bid'] + '"'
    result = orientClient.query(cmd)
    if len(result) == 1:
        print 'pass'
        continue
    else:
        print book['bid'], book['title']
        command = 'create vertex Book set bid="' + book['bid'] + '", title=\'' + book['title'].replace('\'', '').replace('\n', '').replace('\\', '') + '\''
        orientClient.command(command)


# 释放orient资源
orientClient.db_close()
