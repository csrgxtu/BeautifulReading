#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: CleanLibPublisher.py
# Desc: 清洗library里面的publisher，清洗规则见teambition上面的数据清洗文档
# Produced By BR
import re
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['bookshelf']
bookc = db['bookful']

books = bookc.find({'rating': {'$exists': 0}})

rating = {
    "average" : "0.0",
    "max" : 10,
    "min" : 0,
    "numRaters" : 0
}
for book in books:
    # print book
    bookc.update_one({'_id': book['_id']}, {'$set': {'rating': rating}})
