#encoding=utf-8

def search(arr,key):
	"""
	复杂度：O(lg(n))
	"""
	left = 0
	right = len(arr) - 1

	while left <= right:
		mid = left + (right - left) // 2
		val = arr[mid]
		if val == key:
			return mid
		elif val < key:
			left = mid + 1
		else:
			right = mid - 1
	return None

if __name__ == '__main__':
	import random
	l = [1,2,5,6,9,12,53,74,81,97,100]
	key = 12
	print l,key
	print search(l,key)

