#encoding:utf-8
import urllib2
def downloadsAndroid(url):
    header={"Android QQ":"User-Agent: MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
}
    request = urllib2.Request(url,   )
