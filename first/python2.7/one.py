#_*_coding:utf-8 _*_
import  urllib2
# 1.初级版
# ull = urllib2.urlopen("http://www.baidu.com/")
# html = ull.read()
# print html

# 2.升级版
ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
#通过urllib.Request()方法构造一个请求对象
# request = urllib2.Request("http://baidu.com/",headers = ua_headers)
#
# response = urllib2.urlopen(request)
#
# html = response.read()
# print response.getcode() #获取响应码
# print response.geturl() #返回实际的url
# print response.info() #http响应报头
#

#3.url转换
import urllib
wd = {"wd":"百度"}
print urllib.urlencode(wd)  #转换成单字符

m = urllib.urlencode(wd)
print urllib.unquote(m)  #转回来
