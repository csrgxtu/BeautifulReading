#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: RetrieveDataFromBookful2CSV.py
# Desc: 按照海叔的要求提取字段从清洗过的bookful表格
# Date: 26/Jul/2016
#
# Produced By BR
from pymongo import MongoClient
import re
import csv

# connect to mongodb
client = MongoClient('mongodb://127.0.0.1:27017/bookshelf')
db = client['bookshelf']
bc = db['bookful']

CSVFile = open('data.csv', 'wt')
writer = csv.writer(CSVFile)
writer.writerow( ('bid', 'rating', 'price', 'pubdate', 'publisher') )
books = bc.find({'bid': {'$exists': 1}, 'rating': {'$exists': 1}, 'price': {'$exists': 1}, 'pubdate': {'$exists': 1}, 'publisher': {'$exists': 1, '$ne': None}})
for book in books:
    print book['_id']
    bid = book['bid']
    if 'rating' in book and book['rating'] and 'average' in book['rating']:
        rating = book['rating']['average'] + '0'
    else:
        rating = 0

    if book['price'] == "" or not book['price']:
        price = 0
    else:
        tmp = re.findall('[\d\.]+', book['price'])
        if len(tmp) == 0:
            price = 0
        else:
            price = tmp[0].replace('..', '.') + '0'
    try:
        if book['pubdate'] and book['pubdate'] != "":
            pubdate = re.findall('[\d\-]+', book['pubdate'])[0]
        else:
            pubdate = '0000-00-00'
    except:
        pubdate = '0000-00-00'

    publisher = book['publisher']

    print rating, price
    writer.writerow( (bid, float(rating), float(price), pubdate, publisher.encode('utf-8')) )
    # record = bid + ',' + str(rating) + ',' + str(price) + ',' +? str(pubdate) + ',' + publisher
    # print type(record)
    # CSVFile.write(record.encode('utf-8'))
    # CSVFile.write('\n')

CSVFile.close()
