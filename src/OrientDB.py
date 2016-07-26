#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: OrientDB.py
# Desc: query
# Date: 23/July/2016
#
# Produced By BR
import pyorient

# connect to orientdb
orientClient = pyorient.OrientDB("192.168.100.2", 2424)
orientSession = orientClient.connect( "root", "archer" )
orientClient.db_open('bookshelf', "root", "archer" )

cmd = 'select from User where user_id="32849571622349cb976259d8ecb56872"'
result = orientClient.query(cmd)
print result[0]

# 释放orient资源
orientClient.db_close()
