#/usr/local/bin/python2.7
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import sys
import time
import gevent
from gevent import monkey;monkey.patch_all()
import urllib
import requests
sys.path.append('/da1/xujiwei/')
import hagent
import socket

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}

def getHspage(soup,website):
	try:
		index = 1
		divs = soup.findAll('li',{'class':'res-list'})
		for div in divs:
			if div.find('span',{'class':'icon-official'}):
				print 'so find index icon',index
				return index
			else:
				i = div.find('p',{'class':'res-linkinfo'})
				cite = i.cite.text.strip().lower()  #查找cite标签中的website,然后和预设的官网对比
				print cite
				if cite in website or website[7:-1] in cite:
					print 'so find index',index
					return index
			index += 1
	except Exception,e:
		print e
	print "so not find!"
	return 0

	
def getBaidupage(soup,website):
	try:
		div = soup.find('div',{'class':'result c-container '})
		icon = div.find('a',{'href':'http://trust.baidu.com/vstar/official/intro?type=gw'}) or div.find('a',{'href':'http://trust.baidu.com/vstar/official/intro'})
		if icon:
			print 'baidu first index icon find'
			return 1
		else:
			div2 = div.find('div',{'class':'f13'})
			cite = div2.a.text.strip().lower()
			if cite in website or website[7:-1] in cite:
				print 'baidu first index find!'
				return 1
	except Exception,e:
		print e
	print 'baidu not find'
	return 0

def openHtml(url,timeout=10,trytime=3):
	if trytime <=0:
		return None
	socket.setdefaulttimeout(timeout)
	try:
		html = requests.get(url,headers=headers,timeout=timeout).text
		return html
	except Exception,e:
		print e
		return 0
	return openHtml(url,timeout,trytime-1)

def getsoOffcialicon(query,soup):
	div = soup.find('span',{'class':'icon-official'})
	if div:
		print query,'so find offcialicon'
		return 1
	else:
		print query,'so not find'
		return 0

def getbdOffcialicon(query,soup):
	div1 = soup.find('a',{'href':'http://trust.baidu.com/vstar/official/intro?type=gw'})
	if div1 or soup.find('a',{'href':'http://trust.baidu.com/vstar/official/intro'}):
		print query,'bd find offcialicon'
		return 1
	else:
		print query,'bd not find'
		return 0

def getdoubleresult(query):
	global result,tiems
	codequery = urllib.quote(query)
	url1 = 'http://www.so.com/s?q='+codequery
	url2  = 'http://www.baidu.com/s?wd='+codequery
	html1 = hagent.GetHaosouHtml(url1,query)
	time.sleep(1)
	html2 = hagent.GetBaiduHtml(url2,query)
	soup1 = BeautifulSoup(html1)
	soup2 = BeautifulSoup(html2)
	k1 = 0
	k2 = 0
	if soup1:
		k1 = getsoOffcialicon(query,soup1)
	if soup2:
		k2 = getbdOffcialicon(query,soup2)
	
	if k1 or k2:
		print query,str(k2),str(k1)
		result.write(query+'\t'+str(k2)+'\t'+str(k1)+'\t'+times+'\n')


querys = open('/da1/xujiwei/officalsite/data/randomwebsite3000')
result = open('/da1/xujiwei/officalsite/data/anyiconshow3000','w')
#resultlog = open('/da1/xujiwei/badcase/officalsite/data/resultlog10000','a')
geventjobs = []
for line in querys.readlines():
	query = line.strip()
	'''
	query = line.split('\t')[0].strip()
	website = line.split('\t')[1].strip()[1:-1]
	if website[-1] != '/':
		website += '/'
	codequery=urllib.quote(query)
	website = website.lower()
	'''
	times = time.strftime("%Y-%m-%d %H:%M:%S")
	print query
	k1 = 0
	k2 = 0
	try:
		geventjobs.append(gevent.spawn(getdoubleresult,query))
	except Exception,e:
	    print e
querys.close()
gevent.joinall(geventjobs)

result.close()
#resultlog.close()

