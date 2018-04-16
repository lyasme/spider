#_*_ coding:utf-8 _*_

import urllib
import urllib2
#1.拼接url
# url = "http://www.baidu.com/s"
#
# keyword = raw_input("请输入需要查询的关键字：")
#
# wd = {"wd" : keyword}
#
# headers = {"User-Agent" : "Mozilla....."}
#
# wd = urllib.urlencode(wd)
#
# fullurl = url + "?" + wd

# print fullurl
# request = urllib2.Request(fullurl,headers=headers)
#
# response = urllib2.urlopen(request)
#
# print response.read()


#爬取百度贴吧
def loadPage(url,filename):
    """
    作用：根据url发送请求，获取服务器响应文件
    url：需要爬取得url地址
    filename:处理的文件名
    """
    print "正在下载" + filename
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    request = urllib2.Request(url,headers = headers)
    return urllib2.urlopen(request).read()


def writePage(html,filename):
    """
    作用:将html内容写入到本地
    html:服务器相应得文件内容
    """
    print "正在保存"+ filename
    with open(r"filename","w") as f:
        f.write(html)
    print "-" * 30

def tiebaSpider(url,beginPage,endPage):
    """

    :param url: 贴吧的爬虫调度器，负责组合处理每个页面的url
    :param beginPage: 起始页结束页
    :param endPage:
    :return:
    """
    for page in range(beginPage,endPage + 1):
        pn = (page -1) * 50
        filename = "第" +str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        # print fullurl
        html = loadPage(fullurl,filename)
        # print html
        writePage(html,filename)

if __name__ =="__main__":
    kw = raw_input("请输入需要爬取得贴吧名称：")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key  = urllib.urlencode({"kw":kw})
    fullurl = url + key
    tiebaSpider(fullurl,beginPage,endPage)



