#coding:utf-8
import urllib2
import cookielib

filepath = "cookies.txt"
cookie = cookielib.LWPCookieJar(filepath) #设置路径
header  = urllib2.HTTPCookieProcessor(cookie) #设置cookie，与网站有关
opener = urllib2.build_opener(header)
response = opener.open("http://www.renren.com/965762971")

cookie.save(ignore_expires=True,ignore_discard=True) #忽视