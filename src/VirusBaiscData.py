#!/usr/local/env python
# encoding=utf-8
#
# Author: Archer Reilly
# File: VirusBasicData.py
# Desc: 导入病毒基本数据
# Date: 23/Sep/2016
#
# Produced By BR
from util import loadSeasons
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import hashlib
from pymongo import MongoClient
import time
import random

client = MongoClient('mongodb://plag:xLuYMSgJ@192.168.200.22:27017/plag')
db = client['plag']
vc = db['virus']
oc = db['order']
ic = db['infected']


#需要填写你的 Access Key 和 Secret Key
access_key = ''
secret_key = ''

#构建鉴权对象
q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = 'brpublic'

# some constants
# ImgPrefix = '/Users/archer/Desktop/data/'
ImgPrefix = '/Users/archer/Desktop/'
UserIds = [
    '57ee6c4db542f80bd8e69746'
    # 'ow3LFjsPqMHXtChFlNgTq3lIlhR0',
    # 'ow3LFjvMxVYb7VV6zhrPyB0eWPOs',
    # 'ow3LFjhtp5B6aRur45nOGR166v9g',
    # 'ow3LFjgR8NN7dc7gwzLL0g2iOu8Y',
    # 'ow3LFjgYVMKoY9JTIOKOgTbWYapA'
    # 'ow3LFjg3r4qazvCvfYmLd7eTII-A',
    # 'ow3LFjsXE67bpIDtZbAx_Cx8oUkg',
    # 'ow3LFjgYVMKoY9JTIOKOgTbWYapA',
]

m = hashlib.md5()

# 对每张图片，上传，插入数据库
Images = loadSeasons('./names.txt')
for img in Images:
    m.update(img)
    imgName =  m.hexdigest() + '.jpg'
    token = q.upload_token(bucket_name, imgName, 3600)
    ret, info = put_file(token, imgName, ImgPrefix + img)
    if ret['key'] == imgName:
        # userid = random.choice(UserIds)
        userid = UserIds[0]
        vid = m.hexdigest()

        data = {}
        data['url'] = 'http://7xj2i2.com2.z0.glb.qiniucdn.com/' + imgName
        data['content'] = ''
        data['type'] = 'img'
        data['vid'] = vid
        data['userid'] = userid
        data['createtime'] = time.time()
        id = vc.insert_one(data).inserted_id
        print id

        odata = {}
        m.update(str(time.time()))
        odata['orderid'] = m.hexdigest()
        odata['userid'] = userid
        odata['vid'] = vid
        odata['createtime'] = time.time()
        odata['fullfill'] = 0
        odata['speed'] = False
        id = oc.insert_one(odata).inserted_id
        print id

        idata = {}
        idata['carryid'] = userid
        idata['vid'] = odata['vid']
        idata['infectid'] = userid
        idata['orderid'] = odata['orderid']
        idata['createtime'] = time.time()
        id = ic.insert_one(idata).inserted_id
        print id
    else:
        print imgName, 'Fail'
