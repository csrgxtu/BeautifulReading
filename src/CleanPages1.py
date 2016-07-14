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
bc = db['bookful']
bdc = db['bookdetail']

# 对于pages为0的，根据isbn13活着isbn10到bookdetail里面拿数据
books = bc.find({'pages': '0'})
for book in books:
    res = bdc.find_one({'pages': {'$exists': 1}, 'isbn': {'$in': [book['isbn10'], book['isbn13']]}})
    try:
        print res['pages']
    except:
        print 'wocao'
