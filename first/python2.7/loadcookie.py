#coding:utf-8
import urllib2
import cookielib

filepath = "cookies.txt"
cookie = cookielib.LWPCookieJar()
cookie.load(filepath,ignore_discard=False,ignore_expires=False)

header = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(header)
response = opener.open("http://www.renren.com/965762971")
print response.read()
#
# header  = urllib2.HTTPCookieProcessor(cookie) #设置cookie，与网站有关
# opener = urllib2.build_opener(header)
# response = opener.open("http://renren.com")