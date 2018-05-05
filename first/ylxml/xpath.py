#coding:utf-8
import lxml
import lxml.etree

html = lxml.etree.parse("index.html")
print type(html)

res = html.xpath("//li") #是一个列表，包含所有元素
print len(res),type(res)
print type(res[0]) #输出类型是节点

print "****1*8***"
print html.xpath("//li/@class") #输出 所有 li里面class的名称

print "****2*8***"
print html.xpath("//li/@text") #输出 所有 li里面text的名称

print "****3*8***"
print html.xpath("//li/a/@href") #输出 所有 li里面a内部href的名称

print "****4*8***"
print html.xpath("//li/a") #li下面有5个节点，每个节点对应一个元素

print "****5*8***"
print html.xpath("//li/a/@href=\"link2.html\"") #输出判断的是否有一个节点


print "****6*8***"
print html.xpath("//li//span/@class") #输出 所有 li里面的所有span里面的class内容


print "****7*8***"
print html.xpath("//li/a//@class") #输出 所有 li的所有节点内部节点a包含的class

print "****8*8***"
print html.xpath("//li") #输出 所有节点
print html.xpath("//li[1]/a/@href")#输出 第一个
print html.xpath("//li[last()]/a/@href")#输出 最后一个
print html.xpath("//li[last()-1]/a/@href")#输出 倒数第二个节点


print "****9*8***"
print html.xpath("//*[@text=\"2\"]/aa//@href") #选text=2的元素
print html.xpath("//*[@text=\"3\"]/@class")
print html.xpath("//*[@class=\"nimei\"]")
print html.xpath("//li/a/text()") #取<>内容
print html.xpath("//li[3]/a/span/text()") #取span里面的内容