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
import time
import datetime

# connect to mongodb
client = MongoClient('mongodb://127.0.0.1:27017/bookshelf')
db = client['bookshelf']
bc = db['bookful']
libc = db['library']

CSVFile = open('data.csv', 'wt')
writer = csv.writer(CSVFile)
writer.writerow( ('bid', 'rating', 'price', 'pages', 'pubdate') )
# books = bc.find({'bid': {'$exists': 1}, 'rating': {'$exists': 1}, 'price': {'$exists': 1}, 'pubdate': {'$exists': 1}, 'publisher': {'$exists': 1, '$ne': None}})
# libs = libc.find({'bid': {'$exists': 1}, 'price': {'$exists': 1}, 'pages': {'$exists': 1}, 'pubdate': {'$exists': 1}})
libs = libc.find({'bid': {'$exists': 1}, 'pubdate': {'$exists': 1}})
# for book in books:
for book in libs:
    print book['_id']
    bid = book['bid']
    if 'rating' in book:
        try:
            rating = re.findall('[\d\.]+', book['rating'])[0]
        except:
            rating = 0
    else:
        rating = 0

    if 'price' in book and book['price']:
        tmp = re.findall('[\d]+\.{1}', book['price'])
        if len(tmp) == 0:
            price = 0
        else:
            price = tmp[0].replace('..', '.') + '0'
    else:
        price = 0

    try:
        if book['pubdate'] and book['pubdate'] != "":
            pubdate = re.findall('[\d\-]+', book['pubdate'])[0]
        else:
            pubdate = '1600-01-01'
    except:
        pubdate = '1600-01-01'

    print pubdate
    if pubdate == '0':
        pubdate = '1600-01-01'

    # if pubdate.count('-') == 1:
    #     pubdate = pubdate + '-01'
    # elif pubdate.count('-') == 0:
    #     pubdate = '1600-01-01'

    pubdate = int(pubdate.replace('-', ''))
    # try:
    #     w = datetime.datetime.strptime(str(pubdate), "%Y-%m-%d")
    # # pubdate = time.mktime(w.timetuple())
    #     pubdate = (w-datetime.datetime(1600,1,1)).total_seconds()
    # except:
    #     pubdate = 0.0

    bookful = bc.find_one({'bid': bid, 'pages': {'$exists': 1}})
    if bookful:
        try:
            if bookful['pages'] != "":
                pages = re.findall('[\d\.]+', bookful['pages'])[0]
            else:
                pages = 0
        except:
            pages = 0
    else:
        pages = 0

    print bid, float(rating), float(price), float(pages), pubdate
    writer.writerow( (bid, float(rating), float(price), float(pages), pubdate ) )

CSVFile.close()
