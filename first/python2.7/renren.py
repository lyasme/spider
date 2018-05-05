#coding:utf-8
import urllib
import urllib2
import cookielib

cookie = cookielib.CookieJar() #创建一个对象存储cookie
cookie_hander = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookie_hander) #打开浏览器，使用cookie
opener.add_handlers = [("User-Agent","Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE" )] #增加一个浏览器模拟

loginurl = "http://www.renren.com/PLogin.do"
data = {"email":"18870755201","password":"yy123456"}
data = urllib.urlencode(data) #编码

request = urllib2.Request(loginurl,data=data) #请求登录，抓取cookie
response = opener.open(request) #载入cookie，登陆

response_index = opener.open("http://www.renren.com/965762971/profile")
print response_index.read()