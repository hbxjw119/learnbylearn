#encoding=utf-8

import Queue
import os

TYPE_C = ['.c','.cpp','.h','.java']
TYPE_PY = ['.py']
TYPE_SH = ['.sh']

COMMENT1 = '/*'
COMMENT2 = '*/'
COMMENT3 = '//'
COMMENT4 = '#'
COMMENT5 = '\'\'\''
END_FILE = 'END'

result = {'total': 0, 'line': 0, 'comment': 0, 'blank': 0}

def crawl_files(path, file_type, comsumer_num, q):
    for r, dir, file in os.walk(path):
        for f in file:
            if os.path.splitext(f)[1] in file_type:
                q.put(os.path.join(r, f))
    for _ in range(comsumer_num):
        q.put(END_FILE)

def calc_file(q):
    global result
    while True:
        f = q.get()
        is_commnet = False
        if f == END_FILE:
            break

        f_type = os.path.splitext(f)[1]
        lines = open(f).readlines()
        result['total'] += len(lines)

        if f_type in TYPE_C:
            for line in lines:
                line = line.strip()
                if not line:
                    result['blank'] += 1
                elif line.startswith(COMMENT1) and line.endswith(COMMENT2):
                    result['comment'] += 1
                elif (line.startswith(COMMENT1) and COMMENT2 not in line)\
                        or (line.startswith(COMMENT2) and COMMENT1 not in line):
                    is_commnet = not is_commnet
                    result['comment'] += 1
                elif line.startswith(COMMENT3) or is_commnet:
                    result['comment'] += 1
                else:
                    result['line'] += 1

        elif f_type in TYPE_PY:
            for line in lines:
                line = line.strip()
                if not line:
                    result['blank'] += 1
                elif COMMENT5 in line:
                    is_commnet = not is_commnet
                    result['comment'] += 1
                elif line.startswith(COMMENT4) or is_commnet:
                    result['comment'] += 1
                else:
                    result['line'] += 1



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

def length_of_last_word(s):
    if len(s) == 0:
        return 0
    l = s.strip().split(' ')
    return len(l[-1])

def search_matrix(matrix, target):
    i = 0
    if matrix == [] or matrix == [[]]:
        return False

    t = matrix[i][-1]
    if target < t:
        if target in matrix[i]:
            return True
    if target > matrix[-1][-1]:
        return False
    elif target == t:
        return True

    else:
        while t < target:
            i += 1
            t = matrix[i][-1]
        if target in matrix[i]:
            return True
        return False

def yanghui_triagle(n):
    res = [[1]]
    if n == 1:
        return res
    if n == 2:
        res.append([1,1])
        return res
    else:
        res = [[1],[1,1]]
        for j in range(2, n):
            pre_line = res[-1]
            cur_line = [1]
            for i in range(len(pre_line)-1):
                cur_line.append(pre_line[i]+pre_line[i+1])
            cur_line.append(1)
            res.append(cur_line)
    return res



def header():
    print '-----------------------------------------'
    print 'simple code statistics tools, v1.0'

def print_res(dir, blank, comment, code, total):
    print '-----------------------------------------'
    print 'dir: %s' % dir
    print 'blank    comment        code     total'
    print '%s        %s             %s       %s' % (blank, comment, code, total)
    print '-----------------------------------------'



if __name__ == '__main__':

    s = ['a','b','c']
    #str_permutation(s, 0, 2)

    m = [
  []
]
    #print search_matrix(m, 20)
    #print yanghui_triagle(7)
    file_type = ['.c','.cpp', '.h', '.java','.py']
    num = 2
    q = Queue.Queue()
    import threading
    path = '/Users/jimmy/link'
    #crawl_files(path, file_type, num, q)
    #calc_file(q)
    t1 = threading.Thread(target=crawl_files, args=(path, file_type, num, q))
    t2 = threading.Thread(target=calc_file, args=(q,))
    t1.start()
    t2.start()
    t2.join()

    header()
    print_res('/home', result['blank'], result['comment'], result['line'], result['total'])

