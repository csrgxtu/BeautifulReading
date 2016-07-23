#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: TransforUser.py
# Desc: 将mongo里面的user转到orientdb里面去
# Date: 23/July/2016
#
# Produced By BR
from pymongo import MongoClient

client = MongoClient('mongodb://linyy:rioreader@192.168.200.22:27017/bookshelf')
db = client['bookshelf']
uc = db['user']

users = uc.find({'user_name': {'$exists': 1}})
for user in users:
    if 'avatar' in user:
        print user['user_id'], user['user_name'], user['avatar']
    else:
        print user['user_id'], user['user_name'], 'no avatar'
