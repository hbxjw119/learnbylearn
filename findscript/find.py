import os,os.path
import re
from stat import *

def find(where = '.*',content = None, start = '.', ext = None, logic = None):
	context = {}    #注意这里字典的妙用
	context['where'] = where
	context['content'] = content
	context['return'] =[]
	context['ext'] = ext
	context['logic'] = logic

	for root,dirs,files in os.walk(start):
		find_files(context,root,files)

	return context['return']

def find_files(context,dir,files):
	for file in files:
		path = os.path.join(dir,file)
		path = os.path.normcase(path)

		stat = os.stat(path)
		size = stat[ST_SIZE]
		try:
			ext = os.path.splitext(file)[1][1:]

		except:
			ext = ''

		if S_ISDIR(stat[ST_MODE]):continue

		if context['logic'] and not context['logic'](locals()):continue

		if context['ext'] and ext != context['ext']:continue

		if not re.search(context['where'],file):continue

		if context['content']:
			f = open(path,'r')
			match = 0
			for l in f.readlines():
				if re.search(context['content'],l):
					match = 1
					break
			f.close()
			if not match:continue

		file_return = (path,file,ext,size)

		context['return'].append(file_return)


