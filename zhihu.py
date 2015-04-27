#! /usr/bin/env python
# coding = utf-8
# author : hbxjw119

'''
抓取知乎用户答案信息的小爬虫
'''

from bs4 import BeautifulSoup
import urllib2
import urllib
import cookielib

zhihu_url = 'http://www.zhihu.com'
zhihu_loginurl = 'http://www.zhihu.com/login'


class Zhihu():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        # install cookie
        jar = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
        hds = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36')
        opener.addheaders = [hds]
        urllib2.install_opener(opener)

    def login(self):
        response = self.opener.open(zhihu_url).read()
        soup = BeautifulSoup(response)
        # fetch the value of _xsrf
        xsf = soup.find('input', attrs = {'name': '_xsrf'})['value']
        postdata = {'_xsrf': xsf,
                    'email': self.email,
                    'password': self.password,
                    'rememberme': 'y'}
        #try to send a request
        try:
            req = urllib2.Request(zhihu_loginurl, urllib.urlencode(postdata))
            self.res = self.opener.open(req).read()
        except Exception, e:
            print 'Failed to login. Error: ', str(e)
            return False

        return True

    def get_homepage(self):
        '''
        获得登陆用户的主页
        '''
        pagesoup = BeautifulSoup(self.res)
        usertag = pagesoup.find('a', class_ = 'zu-top-nav-userinfo')
        owner_home_page = zhihu_url + usertag['href']
        return owner_home_page

    def input_user_name(self):
        username = raw_input('Input the username want to check:')
        return username


    def get_userinfo(self):
        '''
        获得指定用户的信息
        '''
        ownerpage = self.get_homepage()
        username = self.input_user_name()
        user_page_url = ownerpage.replace('xu-ji-wei-67', username)
        user_ask_url = user_page_url + '/asks'
        user_answers_url = user_page_url+ '/answers'
        user_collections_url = user_page_url + '/collections'
        return (user_page_url, user_ask_url, user_answers_url, user_collections_url)

    def get_answer_list(self,user_ask_url):
        '''
        获取用户答案，问题链接，题目，获赞数，
        '''
        anspage = urllib2.urlopen(user_ask_url).read()
        anssoup = BeautifulSoup(anspage)
        answer_num = anssoup.find('a', {'class': 'item active'}).span.string
        print user_ask_url.split('/')[-2] + 'has ' + answer_num + ' answers totally'
        
        #获得答案的总页数
        answer_pages = round(float(answer_num) / 20)
        
        #如果答案只有一页
        if not answer_pages:
            answer_page = urllib2.urlopen(user_ask_url)
            people_answers_soup = BeautifulSoup(answer_page)
            l = people_answers_soup.find_all('div', class_='zm-item')
            for it in l:
                question_url = zhihu_url + it.a['href']
                voteable = it.find('a', {'name': 'expand'})
                vote = voteable['data-votecount']
                print question_url, it.a.text, vote
                
                answer_soup = BeautifulSoup(urllib2.urlopen(question_url))
                answer_contentlist = answer_soup.find_all('div',class_='zm-editable-content')
                answer_content = answer_contentlist[-1].text
                print answer_content.replace('\n',' ')
                
        else:        
            for i in range(1, int(answer_pages + 1)):
                current_url = user_ask_url + '?page=' + str(i)
                try:
                    current_page = urllib2.urlopen(current_url)
                    people_answers_soup = BeautifulSoup(current_page)
                    l = people_answers_soup.find_all('div', {'class': 'zm-item'})
                    for it in l:
                        question_url = zhihu_url + it.a['href']
                        voteable = it.find('a', {'name': 'expand'})
                        if voteable:
                            vote = voteable['data-votecount']
                        else:
                            vote = 0
                        print question_url, it.a.text, vote

                        answer_soup = BeautifulSoup(urllib2.urlopen(question_url))
                        answer_content = answer_soup.find_all('div',class_='zm-editable-content')[-1].text
                        print answer_content.replace('\n',' ')

                except Exception, e:
                    print 'error' + str(e)
                    
    def writetotxt(self)


if __name__ == '__main__':
    email = raw_input('input your eamil:')
    password = raw_input('input your password:')
    zhihu = Zhihu(email,password)
    if zhihu.login():
        print 'login success!'
        usertuple = zhihu.get_userinfo()
        zhihu.get_answer_list(usertuple[2])




