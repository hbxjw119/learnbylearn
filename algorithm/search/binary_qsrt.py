#encoding=utf-8

def qsrt(m):
	if m < 0:
		raise TypeError('input should not less than 0!')
	left = 0
	right = m
	while abs(right - left) > 1.0e-6: #浮点数比较
		mid = left + (right - left) / 2.0
		if mid * mid > m:
			right = mid
		else:
			left = mid
	return mid

if __name__ == '__main__':
	print qsrt(13)
