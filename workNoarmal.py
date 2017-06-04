import random
import urllib.request
import re
import urllib.request
import urllib
from collections import deque
import time
from urllib import request
import gevent
from gevent import monkey;
import socket

Def_Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
Def_Accept_Encoding = 'gzip, deflate, sdch'
Def_Accept_Language = 'zh-CN,zh;q=0.8'
Def_USer_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
Def_Pic_Dir = r'F:\pcimage'  # 下载的文件夹
# Images_File_Path = r'F:\images.txt'  # 下载的文件夹
Images_File_Path = r'F:\meikong.txt'  # 下载的文件夹


def find():
    queue = deque()
    visited = set()
    url = "xx"
    queue.append(url)
    count = 0
    while queue:
        url = queue.popleft()
        visited |= {url}  # 标记为已访问
        print('已经抓取 %s  ,正在抓取 ……%s' % (count, url))
        count += 1
        req = urllib.request.Request(url)
        req.add_header('User-Agent', Def_USer_Agent)
        try:
            urlop = request.urlopen(req)
            if 'html' not in urlop.getheader(name="Content-Type"):
                continue
            data = urlop.read().decode('utf-8')
            urlop.close()
            # downLoadImage(data)
            saveImageUrl(data)

        except Exception as e:
            print(e)
            continue

        linker = re.compile('href=\"(.+?)\"')
        findlist = linker.findall(data)
        print("匹配到了   %s" % len(findlist))
        for x in findlist:
            if '.css' not in x and x not in visited:
                if "xxx.xxx" in x:
                    queue.append(x)
                else:
                    queue.append("http://xxx.xxx" + x)
                print(" ``````加入队列------>" + x)


def saveImageUrl(data):
    reg = r'http[s]?://.+?.jpg'
    imgreg = re.compile(reg)
    imglist = re.findall(imgreg, data)
    f = open(Images_File_Path, "a")
    try:
        print("找到图片%s" % len(imglist))
        f.writelines('\n'.join(imglist))
    except Exception as  e:
        print(e)
        pass
    finally:
        f.close()
        pass


def downLoadImage(data):
    # # url = "xxx"
    # req = urllib.request.Request(url)
    # req.add_header('User-Agent', Def_USer_Agent)
    # data = request.urlopen(req).read().decode("utf-8")
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
    try:
        urllib.request.urlretrieve(url=imgurl,
                                   filename=Def_Pic_Dir + '\%s.jpg' % random.randint(12, 997984523345234534745362360))
    except Exception as e:
        print(e)
        pass


socket.setdefaulttimeout(10.0)
monkey.patch_all()
find()
