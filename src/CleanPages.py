#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: CleanPages.py
# Desc: 清洗数据库中的pages字段，这些字段可能来自bookful，bookdetail
# Produced By BR
import re
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['bookshelf']
# bc = db['bookful']
bc = db['bookdetail']

# 对于pages不存在的，设置为0
# books = bc.find({'pages': {'$exists': 0}})
# print books.count()
# for book in books:
#     bc.update_one({'_id': book['_id']}, {'$set': {'pages': '0'}})

# 对于pages为“”的，设置为0
# books = bc.find({'pages': {'$exists': 1, '$eq': ''}})
# print books.count()
# for book in books:
#     bc.update_one({'_id': book['_id']}, {'$set': {'pages': '0'}})

# 去除含有汉子"页"和空格的pages
REGEX = re.compile('[ |页]')
books = bc.find({'pages': {'$regex': REGEX}})
print books.count()
for book in books:
    matchObj = re.match(r'(\d+)\g', book['pages'], re.M|re.I)
    if matchObj:
        print book['pages']
        print matchObj.group(1)
        bc.update_one({'_id': book['_id']}, {'$set': {'pages': matchObj.group(1)}}   )
    else:
        print book['pages']
        print 'not match'


# var cursor = db.bookful.find({pages: /[ |页]/})
# while (cursor.hasNext()) {
#   x = cursor.next()
#   regex = /(\d+).$/g
#   x['pages'] = regex.exec(x['pages'])[1]
#   db.bookful.update({'_id': x['_id']}, {$set: {pages: x['pages']}})
# }
