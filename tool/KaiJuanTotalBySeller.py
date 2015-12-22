#!/usr/bin/env python
# coding=utf-8
# Author: Archer Reilly
# File: KaiJuanTotalBySeller.py
# Date: 22/Dec/2015
# Desc: 对开卷的所有书籍，统计各个图书商的总销售价钱
#
# Produced By BR
import unirest
import json

Headers = {
    # 'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# get data from Sauron's datas according to the spider name
#
# spider
# return dict
def getDatas(spider, start, offset):
    rtv = {}
    url = 'http://192.168.100.3:5000/data?start=' + str(start) + '&offset=' + str(offset) + '&spider=' + spider
    unirest.timeout(180)
    res = unirest.get(url, headers=Headers)

    if res.body['code'] != 200:
        return False

    rtv['spider'] = spider
    rtv['start'] = start
    rtv['offset'] = offset
    rtv['datas'] = []
    for item in res.body['data']:
        tmpRtv = {}
        tmpRtv['ISBN'] = item['data']['ISBN']
        # 书籍购买来源
        tmpRtv['data'] = item['data'][u'\u4e66\u7c4d\u8d2d\u4e70\u6765\u6e90']
        rtv['datas'].append(tmpRtv)
    return rtv

# Get Data from Sauron's Data

# Foreach record, process it and put into matrix

# When matrix is ready, count total for each seller,
# and put it into matrix, and put it into file

if __name__ == '__main__':
    res = getDatas('6w', 0, 2)
    # for key in res:
    #     if key == 'ISBN':
    #         print key
    #     elif key == u'\u4e66\u7c4d\u8d2d\u4e70\u6765\u6e90':
    #         print key

    print res
    # print res.keys()
    # for key in res.keys():
    #     if key ==
    # print res
    # print res.has_key('ISBN')
    # print u'书籍购买来源'.encode('unicode-escape')
    # print res.has_key(u'书籍购买来源'.encode('unicode-escape'))
    # print res.has_key(unicode('书籍购买来源'))
