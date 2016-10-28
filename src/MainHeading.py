#!/usr/bin/env python
# encoding=utf-8
#
# Author: Archer Reilly
# File: MainHeading.py
# Date: 29/Sep/2016
# Desc: 将bookdetail里面对应的main_heading更新到bookful中
#
# Produced By BR
from pymongo import MongoClient

# connect to mongodb
# client = MongoClient('mongodb://192.168.100.2:27017/bookshelf')
client = MongoClient('mongodb://rio:VFZPhT7y@192.168.200.22:27017/bookshelf')
db = client['bookshelf']
bc = db['bookful']
dc = db['bookdetail']

for b in bc.find({'main_heading': {'$exists': False}, 'isbn13': {'$exists': True}}).batch_size(50):
    try:
        isbn = b['isbn13']
        d = dc.find_one({'isbn': isbn})
        main_heading = d['main_heading']
        bc.update({'_id': b['_id']}, {'$set': {'main_heading': main_heading}}, upsert=False, multi=False)
        print b['_id'], 'ok'
    except:
        print b['_id'], 'fail'

for b in bc.find({'main_heading': {'$exists': False}, 'isbn10': {'$exists': True}}).batch_size(50):
    try:
        isbn = b['isbn10']
        d = dc.find_one({'isbn': isbn})
        main_heading = d['main_heading']
        bc.update({'_id': b['_id']}, {'$set': {'main_heading': main_heading}}, upsert=False, multi=False)
        print b['_id'], 'ok'
    except:
        print b['_id'], 'fail'
