#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: UserFriendUser.py
# Desc: 建立user到user的关系
# Date: 24/July/2016
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

# 从每条follow记录中解析用户书籍关系
follows = fc.find({'follow_id': {'$exists': 1}, 'followed_id': {'$exists': 1}})
for follow in follows:
    # check if friends，互相关注才是朋友
    aid = follow['follow_id']
    bid = follow['followed_id']
    result = fc.find_one({'follow_id': bid, 'followed_id': aid})
    if type(result) == dict:
        try:
            cmd = 'create edge UserFriendUser from (select from User where user_id="' + aid + '") to (select from User where user_id="' + bid + '")'
            orientClient.command(cmd)
            print aid, bid, 'friends'
        except:
            print aid, bid, 'vertex not exist'
    else:
        print aid, bid, 'not friends'


# 释放orient资源
orientClient.db_close()
