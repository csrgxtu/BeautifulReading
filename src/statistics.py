#!/usr/bin/env python
# coding=utf-8
from pymongo import MongoClient
from util import saveMatrixToFile

f = open('userids.txt', 'r')
userids = f.read().split('\n')[0:-1]
f.close()

client = MongoClient('mongodb://linyy:rioreader@192.168.200.22:27017/bookshelf')
db = client['bookshelf']
userc = db['userext']
libc = db['library']

mat = []
mat.append(['mobile_number', 'keep_books', 'byBarcode', 'byBarcodeP', 'bySSF', 'bySSFP', 'bySpine', 'bySpineP', 'byDouban', 'byDoubanP', 'byManual', 'byManualP', 'ByBarcode', 'ByBarcodeP', 'byShow', 'byShowP', 'byMerge', 'byMergeP', 'unknown', 'unknownP'])
for userid in userids:
    # get basic info
    user = userc.find_one({"user_id": userid})
    # print user['user_name'], user['mobile_number'], user['keep_books']

    # byBarcode
    byBarcode = libc.find({'createtime': {'$lt': '1456761600000'}, "user_id": userid, "sources": "byBarcode"}).count()

    # bySSF
    bySSF = libc.find({'createtime': {'$lt': '1456761600000'}, "user_id": userid, "sources": "bySSF"}).count()

    # bySpine
    bySpine = libc.find({'createtime': {'$lt': '1456761600000'}, "user_id": userid, "sources": "bySpine"}).count()

    # byDouban
    byDouban = libc.find({'createtime': {'$lt': '1456761600000'}, "user_id": userid, "sources": "byDouban"}).count()

    # byManual
    byManual = libc.find({'createtime': {'$lt': '1456761600000'}, "user_id": userid, "sources": "byManual"}).count()

    # ByBarcode
    ByBarcode = libc.find({'createtime': {'$lt': '1456761600000'}, "user_id": userid, "sources": "ByBarcode"}).count()

    # byShow
    byShow = libc.find({'createtime': {'$lt': '1456761600000'}, "user_id": userid, "sources": "byShow"}).count()

    # byMerge
    byMerge = libc.find({'createtime': {'$lt': '1456761600000'}, "user_id": userid, "sources": "byMerge"}).count()

    # unknown
    unknown = libc.find({'createtime': {'$lt': '1456761600000'}, "user_id": userid, "sources": "unknown"}).count()

    if user['keep_books'] == 0:
        user['keep_books'] = 1.0
    else:
        user['keep_books'] = float(user['keep_books'])

    tmp = []
    # tmp.append(user['user_name'])
    tmp.append(user['mobile_number'])
    tmp.append(user['keep_books'])
    tmp.append(byBarcode)
    tmp.append(float(byBarcode/user['keep_books']))
    tmp.append(bySSF)
    tmp.append(float(bySSF/user['keep_books']))
    tmp.append(bySpine)
    tmp.append(float(bySpine/user['keep_books']))
    tmp.append(byDouban)
    tmp.append(float(byDouban/user['keep_books']))
    tmp.append(byManual)
    tmp.append(float(byManual/user['keep_books']))
    tmp.append(ByBarcode)
    tmp.append(float(ByBarcode/user['keep_books']))
    tmp.append(byShow)
    tmp.append(float(byShow/user['keep_books']))
    tmp.append(byMerge)
    tmp.append(float(byMerge/user['keep_books']))
    tmp.append(unknown)
    tmp.append(float(unknown/user['keep_books']))
    print tmp
    mat.append(tmp)

saveMatrixToFile('statistics.csv', mat)
