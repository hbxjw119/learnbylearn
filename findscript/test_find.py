import unittest
import find
import os,os.path

def filename(ret):
	return ret[1]

class FindTest(unittest.TestCase):
	def setUp(self):
		os.mkdir('_test')
		os.mkdir(os.path.join('_test','subdir'))
		f = open(os.path.join('_test','file1.txt'),'w')
		f.write("""first line
		second line
		third line
		fourth line""")
		f.close()
		
		f = open(os.path.join('_test','file2.py'),'w')
		f.write("""this is a test file.
		it has many words in it.
		this is the final line.""")
		f.close()

	def tearDown(self):
		os.unlink(os.path.join('_test','file1.txt'))
		os.unlink(os.path.join('_test','file2.py'))
		os.rmdir(os.path.join('_test','subdir'))
		os.rmdir('_test')

	def testSearchAll(self):
		'''
		test searching all files.
		'''
		res = find.find(r'.*',start = '_test')
		self.assertEqual(map(filename,res),['file1.txt','file2.py'])

	def testSearchFlieName(self):
		'''test searching for specific file by regexp'''
		res = find.find(r'file',start = '_test')
		self.assertEqual(map(filename,res),['file1.txt','file2.py'])
		res = find.find(r'py$',start = '_test')
		self.assertEqual(map(filename,res), ['file2.py'])

	def testSearchByContent(self):
		'''test searching by content'''
		res = find.find(start = '_test',content = 'first')
		self.assertEqual(map(filename,res),['file1.txt'])
		res = find.find(where = 'py$', start = '_test', content = 'line')
		self.assertEqual(map(filename,res) , ['file2.py'])
		res = find.find(where = 'py$', start = '_test', content = 'second')
		self.assertEqual(len(res) , 0)

	def testSearchByExtension(self):
		'''test searching by file extension'''
		res = find.find(start = '_test', ext = 'py')
		self.assertEqual(map(filename,res) , ['file2.py'])
		res = find.find(start = '_test', ext = 'txt')
		self.assertEqual(map(filename,res) , ['file1.txt'])

	def testSearchByLogic(self):
		'''test searching by a logical'''
		res = find.find(start = '_test', logic = lambda x:x['size'] < 50)
		self.assertEqual(map(filename,res) , ['file1.txt'])

if __name__ == '__main__':
	unittest.main()

		

