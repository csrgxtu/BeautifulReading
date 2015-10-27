#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 27/Aug/2015
# File: cookies.py
# Desc: urllib2 cookie test
#
# Produced By CSRGXTU
import urllib2

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'shaishufang=Mjc5MTYwfGZmY2VmYzIyYmMxZjhlZThjNzgzYjFlOGIxOWUwODg2'))
f = opener.open("http://shaishufang.com/index.php/site/main/uid/74557/status//category//friend/false")
with open("test.html", "w") as fh:
    fh.write(f.read())
