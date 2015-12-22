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
import urlparse
import Utility import saveMatrixToFile

Headers = {
    # 'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Get Data from Sauron's Data
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
        if item['data'].has_key('ISBN'):
            tmpRtv['ISBN'] = item['data']['ISBN']
        else:
            continue
        # 书籍购买来源
        tmpRtv['data'] = item['data'][u'\u4e66\u7c4d\u8d2d\u4e70\u6765\u6e90']
        rtv['datas'].append(tmpRtv)
    return rtv


# Foreach record, process it and put into matrix
def processRecord(rtvDict):
    mat = []
    # jingdong dangdang wenxuan joyo bookschina beifa bookuu taoshu chinapub
    vendors = ['jingdong', 'dangdang', 'wenxuan', 'joyo', 'bookschina', 'beifa', 'bookuu', 'taoshu', 'chinapub']
    for data in rtvDict['datas']:
        tmpLst = []
        tmpLst.append(data['ISBN'])
        tmpDict = {}
        for link in data['data']:
            parsed = urlparse.urlparse(str(link))
            if urlparse.parse_qs(parsed.query).has_key('vendor'):
                tmpDict[urlparse.parse_qs(parsed.query)['vendor'][0]] = urlparse.parse_qs(parsed.query)['price'][0]
                # print data['ISBN'], urlparse.parse_qs(parsed.query)['vendor'][0], urlparse.parse_qs(parsed.query)['price'][0]
            # print urlparse.parse_qs(parsed.query).has_key('vendor')
            # print urlparse.parse_qs(parsed.query)['vendor']
        # print tmpDict
        for vendor in vendors:
            if tmpDict.has_key(vendor):
                tmpLst.append(float(tmpDict[vendor])/100)
            else:
                tmpLst.append('0.0')

        # print tmpLst
        mat.append(tmpLst)
    # pass
    return mat

# When matrix is ready, count total for each seller,
# and put it into matrix, and put it into file
def Total(mat):
    Sums = ['Total']
    vendors = ['jingdong', 'dangdang', 'wenxuan', 'joyo', 'bookschina', 'beifa', 'bookuu', 'taoshu', 'chinapub']
    for index in range(1, len(vendors)):
        sum = 0
        for row in mat:
            sum = sum + float(row[index])
        # print sum
        Sums.append(sum)

    return Sums

if __name__ == '__main__':
    Mat = []

    for page in range(1, 2365):
        print 'Page: ', page
        res = getDatas('6w', page, 25)
        mat = processRecord(res)
        for row in mat:
            Mat.append(row)

    Mat.append(Total(Mat))
    saveMatrixToFile('./6wstatistics.csv', Mat)
    # res = getDatas('6w', 0, 5)
    # mat = processRecord(res)
    # print mat
    # Total(mat)
    # for key in res:
    #     if key == 'ISBN':
    #         print key
    #     elif key == u'\u4e66\u7c4d\u8d2d\u4e70\u6765\u6e90':
    #         print key

    # print res
    # print res.keys()
    # for key in res.keys():
    #     if key ==
    # print res
    # print res.has_key('ISBN')
    # print u'书籍购买来源'.encode('unicode-escape')
    # print res.has_key(u'书籍购买来源'.encode('unicode-escape'))
    # print res.has_key(unicode('书籍购买来源'))
