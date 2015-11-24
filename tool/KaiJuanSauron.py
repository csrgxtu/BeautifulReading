#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: KaiJuanSauron.py
# Date: 24/Nov/2015
# Desc: get isbns from /data/kaijuan.csv and build up
#     douban book url and insert into Sauron master db
#
# Produced By BR
import unirest
import json

Headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# putUnvisitedUrls will put data dict to master
# data: {'urls': [{'url': 'http://w.g.com', 'spider': 'Shaishufan'}]}
def putUnvisitedUrls(data):
    url = 'http://192.168.100.3:5000/unvisitedurls'
    unirest.timeout(180) # time out 180 same with scrapy download middlewares
    res = unirest.put(url, headers=Headers, params=json.dumps(data))

    if res.body['code'] != 200:
        return False

    return True

BaseUrl = 'http://book.douban.com/isbn/'

with open('../data/kaijuan.csv', 'r') as FH:
    FH.readline() # remove first line, the header
    counter = 0
    URLS = []

    for line in FH:
        if counter == 1000 or line == '':
            data = {'urls': []}
            for url in URLS:
                data['urls'].append({'url': url, 'spider': '6w'})

            if putUnvisitedUrls(data):
                print 'Inserted: ', len(data['urls'])
            else:
                print 'Fail: ', len(data['urls'])

            counter = 0
            URLS = []

        URLS.append(BaseUrl + line.strip('\n').split(',')[0])
        counter = counter + 1
