#! /usr/bin/env python
#coding=utf-8

import string,sys,pickle,cmd,os
class Phonebook():
	def __init__(self):
		print('my phonebook')
		if not os.path.exists(r'phonebook.txt'):
			self.people = {}
		else:
			self.people = {}
			f = open('phonebook.txt','r')
			self.people = {k.strip() : v.strip() for k,v in (l.split(' ') for l in f.readlines())}
			# for l in f.readlines():
			# 	c = l.rstrip('\n')
			# 	c = c.split(' ')
			# 	self.people[c[0]] = c[1]
			f.close()

	def do_add(self,name):
		if name == '':
			name  = input('inter name you want to add:')
			phone = input('enter the phone:')
			self.people[name] = phone
			f = open('phonebook.txt','a')
			f.write(name + ' ' + phone + '\n')
			print('add succeed!')
			f.close()
			return

	def do_find(self,name):
		if self.people == {}:
			print('no friend corrently!')
			return
		if name == '':
			name = input('enter name you want to find:')
		if name in self.people:
			print('the number of %s is %s' % (name,self.people[name]))
		else:
			print('dont find the number!')

	def do_del(self,name):
		if self.people == {}:
			print('no friend corrently!')
		if name == '':
			name = input('enter name you want to del:')
			if name in self.people:
				del self.people[name]
				f = open('phonebook.txt','w')
				for k in self.people.keys():
					f.write(k + ' ' + self.people[k] + '\n')
				print('delete succeed')
			else:
				print('don\'t exist the name')
	def pri(self):
		if self.people == {}:
			print('no friend corrently!')
			return
		for i in self.people.keys():
			print(i,self.people[i])


if __name__ == '__main__':
	r = Phonebook()
	while(1):
		a = input('enter:')
		if a == '1':
			r.do_add('')
		elif a == '2':
			r.do_find('')
		elif a == '4':
			r.do_del('')
		elif a == '3':
			r.pri()
		else:
			break
