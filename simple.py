# urllib的基本是使用
import re
import urllib

# 熟悉urllib最基本的api
from collections import deque
from urllib import request


def test1():
    url = "http://news.dbanotes.net"
    dataresponse = urllib.request.urlopen(url)
    print(type(dataresponse))
    print(dir(dataresponse))
    print(dataresponse.geturl())
    print(dataresponse.getcode())
    data = dataresponse.read()
    data = data.decode('UTF-8')
    print(data)


# urilib get请求拼接参数
def test2():
    data = {}
    data['word'] = 'Jecvay Notes'
    url_values = urllib.parse.urlencode(data)
    url = "http://www.baidu.com/s?"
    full_url = url + url_values
    print("要请求的地址是" + full_url)
    data = urllib.request.urlopen(full_url).read()
    data = data.decode('UTF-8')
    print(data)


# 简单 宽度优先 爬
def search():
    queue = deque()
    visited = set()
    url = 'http://news.dbanotes.net'  # 入口页面, 可以换成别的'
    queue.append(url)
    count = 0
    while queue:
        url = queue.popleft()
        visited |= {url}  # 标记为已访问
        try:
            print('已经抓取 %s  ,正在抓取 ……%s' % (count, url))
            count += 1
            req = urllib.request.Request(url)
            req.add_header('User-Agent',
                           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36")

            urlop = request.urlopen(req)
            if 'html' not in urlop.getheader(name="Content-Type"):
                continue
            data = urlop.read().decode('utf-8')
        except:
            continue
        linker = re.compile('href=\"(.+?)\"')
        for x in linker.findall(data):
            if 'http' in x and x not in visited:
                queue.append(x)
                print(" ``````加入队列------> " + x)
