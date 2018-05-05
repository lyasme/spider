#encoding:utf-8
import urllib2

class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        res = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        res.status=code
        res.newurl=res.geturl()
        print res.newurl,res.status
        return res

opener = urllib2.build_opener(RedirectHandler)
opener.open("http://www.baidu.cn/")
