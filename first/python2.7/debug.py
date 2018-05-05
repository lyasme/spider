#coding:utf-8
import urllib2
httpHander =urllib2.HTTPHandler(debuglevel=1)
httpsHander=urllib2.HTTPSHandler(debuglevel=1) #输出调试信息

operner = urllib2.build_opener(httpHander,httpsHander)
urllib2.install_opener(operner) #全局生效

response = urllib2.urlopen("http://www.renren.com/")