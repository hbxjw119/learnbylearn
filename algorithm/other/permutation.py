#encoding=utf-8

def swap(str_list, i, j):
    str_list[i], str_list[j] = str_list[j], str_list[i]

# 全排列
def str_permutation(str_list, begin, end):
    if str_list is not None and end >= begin and end < len(str_list) and begin >=0:
        if begin == end:
            print str_list
        else:
            for i in range(begin, end + 1):
                swap(str_list, i, begin)
                str_permutation(str_list, begin + 1, end)
                swap(str_list, begin, i)

if __name__ == '__main__':
    s = ['a','b','c']
    str_permutation(s, 0, 2)
