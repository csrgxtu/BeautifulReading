#!/usr/bin/env python
# coding=utf8
# Author: Archer Reilly
# File: InsertBIDS.py
# Desc: Insert bid into a article in bookshelf.article according to the id
#
# Produced By BR
from Utility import loadSeasons
from pymongo import MongoClient
from bson.objectid import ObjectId

# load bids
BIDS = loadSeasons('./BIDS.txt')

# connect to mongodb
client = MongoClient('mongodb://rio:VFZPhT7y@192.168.200.22:27017/bookshelf')
#client = MongoClient('mongodb://192.168.100.2:27017/bookshelf')
db = client['bookshelf']
collection = db['article']

ID = '5761557e05cf2806003e1367'

for bid in BIDS:
    # coll.update({'ref': ref}, {'$push': {'tags': new_tag}})
    print 'Append bid to article.related_books', bid
    collection.update({'_id': ObjectId(ID)}, {'$push': {'related_books': bid}})
