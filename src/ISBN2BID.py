#!/usr/local/env python
# coding=utf-8
#
# Author: Archer
# File: ISBN2BID.py
# Desc: 批量转换isbn到bid
# Date: 4/Aug/2016
from pymongo import MongoClient

client = MongoClient('mongodb://rio:VFZPhT7y@192.168.200.22:27017/bookshelf')
db = client['bookshelf']
bookc = db['bookful']

ISBNS = []
with open('/Users/archer/Downloads/织女.csv') as F:
    for line in F:
        ISBNS.append(line.split(',')[0])

print ISBNS

BIDS = []
for isbn in ISBNS:
    res = bookc.find_one({'isbn13': isbn})
    print res['bid']
    BIDS.append(res['bid'])

with open('bids.csv', 'w') as F:
    for bid in BIDS:
        F.write('"' + bid + '",')
