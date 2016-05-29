#/usr/local/bin/python2.7
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import sys
import urllib2
import urllib
import socket 
import random
import agent
reload(sys)
sys.setdefaultencoding('utf8')

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}


def openHtml(url,timeout=10,trytime=3):
   if trytime <=0:
      return '0'
   socket.setdefaulttimeout(timeout)
   try:
      req = urllib2.Request(url,headers=headers)
      html = urllib2.urlopen(req,timeout=5).read()
      return html
   except Exception,e:
      return '0'
   return openHtml(url,timeout,trytime-1)


url = 'http://www.lvse.com/all/p1/'
urls = ['http://www.lvse.com/all/in-p'+str(i)+'/' for i in range(9001,9798)]
webfile = open('/da1/xujiwei/badcase/officalsite/data/websitequery10','w')
for url in urls:
	print url
	try:
		html = openHtml(url)
		if html == '0':
			ip_pos = random.randint(0,len_ip_value-1)
			html = agent.GetHtmlDaili(url,ip_value[ip_pos])
		if html != '0':
			soup = BeautifulSoup(html)
			movietypes = soup.findAll('div',{'class':'info'})
			for item in movietypes:
				title = item.findAll('a',{'target':'_blank'}) 
				if title:
					webfile.write(title[0].next+'\t'+title[1].next+'\n')
					print title[0].next+'\t'+title[1].next
	except Exception,e:
			print e

webfile.close()

