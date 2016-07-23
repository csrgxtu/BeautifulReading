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
import pyorient

# connect to mongodb
client = MongoClient('mongodb://linyy:rioreader@192.168.200.22:27017/bookshelf')
db = client['bookshelf']
uc = db['user']

# connect to orientdb
orientClient = pyorient.OrientDB("192.168.100.2", 2424)
orientSession = orientClient.connect( "root", "archer" )
orientClient.db_open('bookshelf', "root", "archer" )


users = uc.find({'user_name': {'$exists': 1}})
for user in users:
    command = ''
    if 'avatar' in user:
        print user['user_id'], user['user_name'], user['avatar']
        command = 'create vertex User set user_id="' + user['user_id'] + '", user_name=\'' + user['user_name'].replace('\'', '').replace('\n', '').replace('\\', '') + '\', avatar="' + user['avatar'] + '"'
    else:
        print user['user_id'], user['user_name'], 'no avatar'
        command = 'create vertex User set user_id="' + user['user_id'] + '", user_name=\'' + user['user_name'].replace('\'', '').replace('\n', '').replace('\\', '') + '\''

    orientClient.command(command)


# 释放orient资源
orientClient.db_close()
