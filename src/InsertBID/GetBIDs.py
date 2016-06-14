#!/usr/bin/env python
# coding=utf8
# Author: Archer Reilly
# File: GetBIDs.py
# Date: 14/6/2016
# Desc: Get bids from database according to isbn
#
# Produced By BR
from Utility import loadSeasons
from pymongo import MongoClient

# load isbns
ISBNS = loadSeasons('./isbns.txt')
# print ISBNS[0]

# connect to mongodb
client = MongoClient('mongodb://linyy:rioreader@192.168.200.20:27017/bookshelf')
db = client['bookshelf']
collection = db['bookful']

for isbn in ISBNS:
    res = collection.find_one({'$or': [{'isbn10': isbn}, {'isbn13': isbn}]})
    if res:
        if res.has_key('bid'):
            print isbn, res['bid']
