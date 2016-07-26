#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: ReadStatusUpdateTime.py
# Desc: 对于阅读状态是reading的如果没有read_status_update_time字段，就使用
# createtime 作为其默认.
# Date: 26/July/2016
#
# Produced By BR
from pymongo import MongoClient

client = MongoClient('mongodb://192.168.100.2:27017/bookshelf')
db = client['bookshelf']
libc = db['library']

libs = libc.find({'read_status': 'reading', 'status': 'visable', 'read_status_update_time': {'$exists': 0}})
for lib in libs:
    print libc.update_one({'_id': lib['_id']}, {'$set': {'read_status_update_time': lib['version']}})
