#coding:utf-8
import urllib2
httpHander =urllib2.HTTPHandler(debuglevel=1)
httpsHander=urllib2.HTTPSHandler(debuglevel=1) #输出调试信息

operner = urllib2.build_opener(httpHander,httpsHander)