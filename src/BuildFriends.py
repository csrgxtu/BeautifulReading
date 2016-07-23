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
fc = db['follow']

# connect to orientdb
orientClient = pyorient.OrientDB("192.168.100.2", 2424)
orientSession = orientClient.connect( "root", "archer" )
orientClient.db_open('bookshelf', "root", "archer" )

follows = fc.find({'followed_id': {'$exists': 1}, 'follow_id': {'$exists': 1}})
for follow in follows:
    aid = follow['follow_id']
    bid = follow['followed_id']
    if fc.find_one({'follow_id': bid, 'followed_id': aid}):
        print 'UserFriendUser', aid, bid
        command = 'create edge UserFriendUser from (select from User where user_id=' + aid + ') to (select from User where user_id=' + bid + ')'
        orientClient.command(command)

# 释放orient资源
orientClient.db_close()
