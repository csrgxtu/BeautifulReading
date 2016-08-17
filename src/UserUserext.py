#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer
# File: UserUserext.py
# Desc: 对比User和Userext，因为有的用户登陆不了
# Date: 17/Aug/2016
from pymongo import MongoClient

client = MongoClient('mongodb://@192.168.200.22:27017/bookshelf')
db = client['bookshelf']
uc = db['user']
uec = db['userext']

users = uc.find({'status': 'visable'})
for user in users:
    res = uec.find_one({'user_id': user['user_id']})
    if not res:
        print user['user_id']
