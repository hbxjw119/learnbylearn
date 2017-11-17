#encoding=utf-8

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
	Given nums = [2, 7, 11, 15], target = 9,

	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
"""

def two_sum(arr,target):
	l = []
	arr.sort()
	for index in range(len(arr)):
		if target - arr[index] in arr[index:]:
			l.append([arr[index],target - arr[index]])

	return l

if __name__ == '__main__':
	l = [4,2,6,1,7,11,8,10]
	print l
	target = 12
	print two_sum(l,target)
