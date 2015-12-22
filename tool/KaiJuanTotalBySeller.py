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
    url = 'http://192.168.100.3:5000/data?start=' + start + '&offset=' + offset + '&spider=' + spider
    unirest.timeout(180)
    res = unirest.get(url, headers=Headers)

    if res.body['code'] != 200:
        return False

    return res.body['data']

# Get Data from Sauron's Data

# Foreach record, process it and put into matrix

# When matrix is ready, count total for each seller,
# and put it into matrix, and put it into file

if __name__ == '__main__':
    getDatas('6w', 0, 1)
