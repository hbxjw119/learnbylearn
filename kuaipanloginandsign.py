#! /usr/bin/env python
#coding=utf-8

import urllib
import urllib2
import cookielib
import json
import re

url = 'http://www.kuaipan.cn'
loginurl = 'http://www.kuaipan.cn/accounts/login/'
class Login_kp():
    
    def login(self,username,password):
        self.name = username
        self.psd = password
        #create cookie object
        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        hds = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36')
        self.opener.addheaders = [hds]
        urllib2.install_opener(self.opener)

        
        print 'wait,login in...'

        try:
            urllib2.urlopen(url)
            postdata = {'username':self.name,'password':self.psd,'isajax':'yes'}
            postdata = urllib.urlencode(postdata)
            req = urllib2.Request(loginurl,postdata)
            fd = urllib2.urlopen(req)

        except:
            print 'Net or other error!'
            return False

        print 'login success!'
        lo = fd.read()
    
        print '***********************************************'
        myurl = 'http://web.kuaipan.cn/n/drive/files' #the home url
        res = urllib2.urlopen(myurl).read()
        p = re.compile(r'b\scsstxt=\"(.*?)\">') #search the space information
        spaceinfo = p.search(res)
        if spaceinfo:
            print spaceinfo.group(1)
        #print res

        print '***********************************************'
        return True

    def logout(self):
        url = 'http://www.kuaipan.cn/index.php?ac=common&op=logout'
        rp = urllib.request.urlopen(url)
        rp.close()
        print('logout succeed!')
        
    def sign(self):
        print 'signing...'
        url2 = 'http://www.kuaipan.cn/index.php?ac=common&op=usersign' #the sign url
        response = urllib2.urlopen(url2)
        sign = response.read().decode('utf-8')
        sign_data = json.loads(sign)

        if sign_data['state'] == -102:
            print 'you have already signed today!'
        elif sign_data['state'] == 1:
            print 'signed succeed!'
        else:
            print 'signed failed!'
        
       
if __name__ == '__main__':
    kk = Login_kp()
    user = input('input your username:')
    pwd = input('input your password:')
    if kk.login(user,pwd):
        kk.sign()
