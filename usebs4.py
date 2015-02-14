__author__ = 'hbxjw119'
#coding=utf-8

from bs4 import BeautifulSoup
import urllib2
import requests

url_hd = 'http://m.weather.com.cn/mweather/101270101.shtml'

def getweatherinfo(url):
    #rep = urllib2.urlopen(url).read()
    r = requests.get(url)
    rep = r.text
    soup = BeautifulSoup(rep)
    weatherinfo = soup.find_all('div',class_='days7')
    
    for item in weatherinfo.find_all('li'):
    	print item.b.string,item.span.string,item.i.img['alt']
	'''
    print day
    print temp
    daylist=[]
    templist = []
    for d in day:
        daylist.append(d.string)
    for t in temp:
        templist.append(t.string)

    print daylist
    print templist
	'''
	

if __name__ == '__main__':
    print u'weather information of chengdu:'
    getweatherinfo(url_hd)

