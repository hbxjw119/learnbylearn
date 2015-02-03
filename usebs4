__author__ = 'hbxjw119'
#coding=utf-8

from bs4 import BeautifulSoup
import urllib2

url_hd = 'http://m.weather.com.cn/mweather/101270101.shtml'

def getweatherinfo(url):
    rep = urllib2.urlopen(url).read()
    soup = BeautifulSoup(rep)
    weatherinfo = soup.find_all('div',class_='days7')
    for tag in weatherinfo:
        day = tag.find_all('b')
        temp = tag.find_all('span')
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
	for i in range(len(day)):
		print day[i].string,temp[i].string

if __name__ == '__main__':
    print u'weather information of chengdu:'
    getweatherinfo(url_hd)

