# 从爬去的图片抵制下载图片
import random
import urllib
from multiprocessing.pool import Pool
from urllib import request
import gevent
import time

from gevent import monkey

Def_USer_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
Def_Pic_Dir = r'F:\pcmeikongimage'  # 下载的文件夹
Images_File_Path = r'F:\meikong.txt'  # 下载的文件夹


def readUrl():
    f = open(Images_File_Path, "r")
    urls = set()
    count = 0;
    for line in f:
        count += 1
        if count > 100:
            break
        print("读取 %s" % str(line))
        urls.add(line)
    f.close()
    return list(urls)


def downLoadImage(urls, name):
    print('Run process      %s ----------> %s ' % (name, len(urls)))
    tasks = []
    x = 0
    for imgurl in urls:
        x += 1
    tasks.append(gevent.spawn(fetch, imgurl, x, name))
    gevent.joinall(tasks)


    # 协程 去下载


async def fetch(imgurl, x, name):
    print("进程 %s 正在下载  %s-----  %s" % (name, x, imgurl))

    opener = request.build_opener()
    opener.addheaders = [('User - Agent', Def_USer_Agent)]
    request.install_opener(opener)
    name = str(time.time()).replace(",", "") + str(random.randint(1, 3426))
    try:
        await urllib.request.urlretrieve(url=imgurl,
                                         filename=Def_Pic_Dir + '\%s.jpg' % name)
    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':
    urls = readUrl()

    ProcessNumber = 8  # 线程数量
    p = Pool(8)  # 线程池的数量
    # 线程平分任务
    pease = len(urls) // ProcessNumber
    for i in range(ProcessNumber):
        p.apply_async(downLoadImage, args=(urls[i * pease: (i + 1) * pease], i))

    # 剩下的给最后一个进程
    if (not (len(urls) % ProcessNumber) == 0):
        p.apply_async(downLoadImage, args=(urls[-(len(urls) % ProcessNumber):], ProcessNumber + 1))

    p.close()
    p.join()
    print('任务完成~')
