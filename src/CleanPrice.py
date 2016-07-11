#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: CleanAuthor.py
# Desc: 清洗数据库中的Author字段，这些字段可能来自library，bookful，bookdetail
# Produced By BR
import re
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['bookshelf']
libc = db['library']

countries = []

libs = libc.find({}, {'price': 1})
print libc.count()
for lib in libs:
    if not 'price' in lib:
        lib['price'] = '0.0 元'

    if not lib['price']:
        lib['price'] = '0.0 元'

    if lib['price'] == "":
        lib['price'] = '0.0 元'

    matchObj = re.match(r'([A-Z|a-z|$]*)([\d|\.]*)(.*)', lib['price'].replace(' ', ''), re.M|re.I)
    prices = []
    if matchObj:
        # print matchObj.group()
        prices.append(matchObj.group(1))
        # print '#' + matchObj.group(2) + '#'
        # print matchObj.group(1)
        prices.append(matchObj.group(2))
        prices.append(matchObj.group(3))

    # for price in prices:
    #     if price == u'':
    #         prices.remove(price)

    if len(prices) == 1:
        prices.append('元')

    if prices[0] == u'':
        prices.remove(prices[0])
    else:
        prices.remove(prices[2])
        prices[0], prices[1] = prices[1], prices[0]

    if prices[1] == u'':
        prices[1] = '元'

    if prices[1] == 'CNY':
        prices[1] = '元'

    try:
        prices[0] = float(prices[0])
    except:
        print prices[0], prices[1]

    print prices[0], prices[1]
    libc.update_one({'_id': lib['_id']}, {'$set': {'price': str(prices[0]) + prices[1]}})
