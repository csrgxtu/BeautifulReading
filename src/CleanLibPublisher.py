#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: CleanLibPublisher.py
# Desc: 清洗library里面的publisher，清洗规则见teambition上面的数据清洗文档
# Produced By BR
import re
from pymongo import MongoClient

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

# 按照规则重新排序出版社信息，筛选出主要出版社及辅助出版社
# 接收无规则的出版社数组，返回有规则的出版社数组
def RearrangePublishers(publishers):
    newPublishers = []
    OriLength = len(publishers)

    # 从publishers里面第一个开始，如果 出版社 书店 书局 书馆
    pubfilter = ['出版社', '书店', '书局', '书馆']
    for pub in publishers:
        if any(x in pub for x in pubfilter):
            newPublishers.append(pub)
            publishers.remove(pub)

    if len(newPublishers) == 0:
        newPublishers = publishers
    elif len(newPublishers) < OriLength:
        newPublishers.extend(publishers)

    return newPublishers

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['bookshelf']
libc = db['library']

REGEX = re.compile('[;|，|,| |\/]')
libs = libc.find({'publisher': {'$regex': REGEX}})
print libs.count()

for lib in libs:
    # 如果里面包含\n，就是空的publisher，需要更新
    if '\n' in lib['publisher']:
        # print 'Update', lib['_id'], None
        # update statements here
        continue

    # 判断是否为英文出版社，若是，do nothing
    if is_ascii(lib['publisher']):
        # print 'English Publisher', lib['_id'], lib['publisher']
        continue

    # 中文的出版社条件比较复杂
    lib['publisher'] = lib['publisher'].replace(',', '#')
    lib['publisher'] = lib['publisher'].replace('/', '#')
    lib['publisher'] = lib['publisher'].replace(' ', '#')
    lib['publisher'] = lib['publisher'].replace('|', '#')
    lib['publisher'] = lib['publisher'].replace(';', '#')
    # lib['publisher'] = lib['publisher'].replace('\uff0c', '#')
    # print lib['_id'], lib['publisher']

    # 根据delimiter分割publisher
    # print filter('', lib['publisher'].split('#'))
    publishers = []
    for pub in lib['publisher'].split('#'):
        if pub != u'':
            publishers.append(pub)

    # convert to UTF8, though print out as utf-8 code
    publishers = [x.encode('UTF8') for x in publishers]
    # if len(publishers) >= 3:
    #     # done
    #     # update statements here
    #     continue
    #
    # print publishers
    newPublishers = RearrangePublishers(publishers)
    for pub in newPublishers:
        print pub,
    print '.'
    newPublishers.append(lib['publisher'])

    # 添加处理后的publish信息到新字段
    # lib['publishers'] = newPublishers
    # 只要update新增的字段publishers就可以了，其它不动
    libc.update_one(
        {"_id": lib['_id']},
        {"$set": {"publishers": newPublishers, "publisher": newPublishers[0]}}
    )
