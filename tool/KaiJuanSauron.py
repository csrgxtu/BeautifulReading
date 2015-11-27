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
    url = 'http://127.0.0.1:5000/unvisitedurls'
    unirest.timeout(180) # time out 180 same with scrapy download middlewares
    res = unirest.put(url, headers=Headers, params=json.dumps(data))

    if res.body['code'] != 200:
        return False

    return len(res.body['data'])

BaseUrl = 'http://book.douban.com/isbn/'

with open('../data/stdkaijuan.csv', 'r') as FH:
    FH.readline() # remove first line, the header
    counter = 0
    URLS = []

    for line in FH:
        if counter == 10 or line == '':
            data = {'urls': []}
            for url in URLS:
                data['urls'].append({'url': url, 'spider': '6w'})

            # data = {'urls': [{'url': 'http://book.douban.com/subject/1078056/', 'spider': '6w'}]}
            ret = putUnvisitedUrls(data)
            # ret = 0
            # print data
            print 'InserteUnvisitedUrls, Trying ', len(data['urls']), ', Actually: ', ret

            counter = 0
            URLS = []
            # break

        URLS.append(BaseUrl + line.strip('\n').split(',')[0])
        counter = counter + 1
