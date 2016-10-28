#!/usr/bin/env python
# encoding=utf-8
#
# Author: Archer
# File: LoadPoemData.py
# Date: 28/Oct/2016
# Desc: 从老的给孩子的诗载入用户数据到微信小程序的给孩子的诗里面
#
# Produced By BR
from pymongo import MongoClient
import MySQLdb

# Open database connection
client = MongoClient('mongodb://192.168.100.2:27017/bookshelf')
db = client['bookshelf']
uc = db['user']
db = MySQLdb.connect("localhost","root","rootroot","br")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM userinfo")

# Fetch a single row using fetchone() method.
results = cursor.fetchall()
for row in results:
    user_id = row[1]
    user_name = row[2]
    password = row[3]
    user_agent = row[4]
    email = row[5]
    mobile = row[6]
    avatar = row[7]
    createtime = row[8]
    updatetime = row[9]
    client_ip = row[10]

    user = {
        "user_id": user_id,
        "user_name": user_name,
        "password": password,
        "user_agent": user_agent,
        # "email": email,
        "mobile_number": mobile,
        "avatar": avatar,
        "createtime": createtime,
        "updatetime": updatetime,
        "client_ip": client_ip,
        "status": "visable",
        "source": "oldPoem"
    }

    id = uc.insert_one(user).inserted_id
    print id

# disconnect from server
db.close()
