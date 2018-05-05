#coding:utf-8
import urllib2
import cookielib

filepath = "baiducookies.txt"
cookie = cookielib.LWPCookieJar()
cookie.load(filepath,ignore_discard=False,ignore_expires=False)

header = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(header)
# response = opener.open("http://www.renren.com/965762971")

response = opener.open("http://www.baidu.com")
print response.read()
