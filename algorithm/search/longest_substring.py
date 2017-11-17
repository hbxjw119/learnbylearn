#encoding=utf-8
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

	Given "abcabcbb", the answer is "abc", which the length is 3.

	Given "bbbbb", the answer is "b", with the length of 1.

	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

def longest_sub(string):
	s = []
	for i in string:
		if i not in s:
			s.append(i)
	return s

if __name__ == '__main__':
	s1 = 'abcabcbb'
	s2 = 'bbbb'
	s3 = 'pwwkew'
	print longest_sub(s1)
	print longest_sub(s2)
	print longest_sub(s3)
