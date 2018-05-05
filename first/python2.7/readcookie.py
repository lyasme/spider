#coding:utf-8
import urllib2
import cookielib  #创建一个cookie对象存储cookie
cookie = cookielib.CookieJar()
header = urllib2.HTTPCookieProcessor(cookie)#自动提取
opener = urllib2.build_opener(header)  #处理cookie
response = opener.open("http://www.renren.com/")
cookies = ""
for data in cookie:
    cookies = cookies + data.name+"="+data.value+";\r\n"
print cookies