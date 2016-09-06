#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: CleanAuthor.py
# Desc: 清洗数据库中的Author字段，这些字段可能来自library，bookful，bookdetail
# Produced By BR
import re
from pymongo import MongoClient

# client = MongoClient('mongodb://rio:VFZPhT7y@192.168.200.22:27017/bookshelf')
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['bookshelf']
bookc = db['bookful']

# 如果作者字段中包含“编”，“著”等非作者名称字样，去除之。主編
REGEX = re.compile('.*[编|編|著|绘|译|等|主编|主編|副主编|编写|译者]+.*')
books = bookc.find({'author': {'$regex': REGEX}}, {'author': 1})
print books.count()
for book in books:
    author = []
    for b in book['author']:
        # print b,
        b = b.encode('utf-8')

        b = b.replace('\xe5\x89\xaf\xe4\xb8\xbb\xe7\xbc\x96', '')
        b = b.replace('\xe8\xaf\x91\xe8\x80\x85', '')
        b = b.replace('\xe4\xb8\xbb\xe7\xbc\x96', '')
        b = b.replace('\xe4\xb8\xbb\xe7\xb7\xa8', '')
        b = b.replace('\xe7\xbc\x96\xe5\x86\x99', '')
        b = b.replace('\xe7\xbc\x96', '')
        b = b.replace('\xe7\xb7\xa8', '')
        b = b.replace('\xe8\x91\x97', '')
        b = b.replace('\xe7\xbb\x98', '')
        b = b.replace('\xe8\xaf\x91', '')
        b = b.replace('\xe7\xad\x89', '')
        # print b,
        author.append(b)
    # print '\n'
    bookc.update_one({"_id": book["_id"]}, {'$set': {'author': author}})
    # print author

# 如果作者名称中包含“（英）”，“［美国］”等表明国家的字样，去除之。
REGEX = re.compile('[\(*\)|\（*\）|\[*\]|\［*\］]+')
books = bookc.find({'author': {'$regex': REGEX}})
print books.count()
for book in books:
    author = []
    for b in book['author']:
        print b
        matchObj = re.match(r'.*([\(|\[].*[\)|\]]+).*', b, re.M|re.I)
        # matchObj = re.match(r'[\(.*\)|\（.*\）|\[.*\]|\［.*\］]*', b, re.M|re.I)
        if matchObj:
            author.append(b.replace(matchObj.group(1), ''))
    bookc.update_one({"_id": book["_id"]}, {'$set': {'author': author}})
