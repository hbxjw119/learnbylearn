#encoding=utf-8

import requests
import time
import random
import threading
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

cnt = 0  #下载的总文件数
size = 0  #下载的文件总大小
l = threading.Lock()

def fetchPage(url):
    global cnt,size,l
    try:
        req = requests.get(url)
        content = req.content
        l.acquire()
        cnt += 1
        size += int(req.headers['Content-Length'])
        l.release()
        #return content
        if req.status_code != 200:
            print url,req.status_code
    except Exception,e:
        print e

if __name__ == '__main__':
    f = open('urllist').readlines()
    slice = f[0:4000000]
    urllist = [i.strip() for i in slice]

    tm = time.time()
    pool = ThreadPool(80)
    try:
        #pool.map(fetchPage,urllist)
        pool.map_async(fetchPage,urllist).get(10000000)
        pool.close()
        pool.join()
    except KeyboardInterrupt:
        print cnt 
        print size / 1024 / 1024  #以M为单位
        print time.time() -tm
        print cnt / (time.time() - tm)  #每秒下载文件个数

    '''
    tm = time.time()
    for i in urllist:
        fetchPage(i)
    print time.time() - tm
    '''
