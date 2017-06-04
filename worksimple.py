# encoding:UTF-8
import urllib.request
import re
import urllib.request
import urllib
from urllib import request
import os
import gevent
from gevent import monkey;

# 这个文件里面是爬取一个网页的图片
# 防止403伪造一个useragnet，
Def_USer_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
Def_Pic_Dir = r'F:\pcimage'  # 下载的文件夹


# 简答的爬取一个网页图片
def projectIndex():
    url = "xx"
    req = urllib.request.Request(url)
    req.add_header('User-Agent', "DEF_USer_Agent")
    data = request.urlopen(req).read().decode("utf-8")
    regstr = r'http://cdn.[a-zA-z0-9]{6}.cc/.{32}'
    imreg = re.compile(regstr)
    imglist = re.findall(imreg, data)
    print("找到 %s个图片" % len(imglist))
    for imgurl in imglist:
        x = imgurl.split("http://cdn.q8oils.cc/")[1]
        print(x)
        urllib.request.urlretrieve(imgurl, Def_Pic_Dir + '\%s.jpg' % x)


# 使用协程序去下载图片。同时 下载时候添加请求头，解决防盗链
def baidutst():
    # url = "http://hc666.com/htm/2017/5/21/p02/376558.html"
    url = "http://www.jjjj98.com/htm/2017/5/21/p01/376472.html"
    req = urllib.request.Request(url)
    req.add_header('User-Agent', Def_USer_Agent)
    data = request.urlopen(req).read().decode("utf-8")
    reg = r'http[s]?://.+?.jpg'
    imgreg = re.compile(reg)
    imglist = re.findall(imgreg, data)
    print("找到%s" % len(imglist))
    x = 0
    tasks = []
    for imgurl in imglist:
        x += 1
        tasks.append(gevent.spawn(fetch, imgurl, x))
    gevent.joinall(tasks)


# 协程 去下载
def fetch(imgurl, x):
    print("正在下载  %s-----  %s" % (x, imgurl))
    opener = request.build_opener()
    opener.addheaders = [('User - Agent', Def_USer_Agent)]
    request.install_opener(opener)
    # try:
    urllib.request.urlretrieve(url=imgurl, filename=Def_Pic_Dir + '\%s.jpg' % x)
    # except:
    #     pass


def start():
    # 先删除目录已经存在的文件
    # files = os.listdir(Def_Pic_Dir)
    # for i in files:
    #     os.remove(os.path.join(Def_Pic_Dir, i))

    monkey.patch_all()
    baidutst()


start()
