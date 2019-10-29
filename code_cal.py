#encoding=utf-8

'''
simple code statistics tools
'''


import Queue
import os
import threading
import sys

TYPE_C = ['.c','.cpp','.h','.java', '.php']
TYPE_PY = ['.py']
TYPE_SH = ['.sh']

FILE_TYPE = ['.c','.cpp', '.h', '.java','.py', '.php']

COMMENT1 = '/*'
COMMENT2 = '*/'
COMMENT3 = '//'
COMMENT4 = '#'
COMMENT5 = '\'\'\''
END_FILE = 'END'

result = {'total': 0, 'line': 0, 'comment': 0, 'blank': 0}
thread_num = 2

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
                if not line.strip():
                    result['blank'] += 1
                elif line.strip().startswith(COMMENT1) and line.strip().endswith(COMMENT2):
                    result['comment'] += 1
                elif (line.strip().startswith(COMMENT1) and COMMENT2 not in line.strip()) or (line.strip().endswith(COMMENT2) and COMMENT1 not in line.strip()):
                    is_commnet = not is_commnet
                    result['comment'] += 1
                elif line.strip().startswith(COMMENT3) or is_commnet:
                    result['comment'] += 1
                else:
                    result['line'] += 1

        elif f_type in TYPE_PY:
            for line in lines:
                if not line.strip():
                    result['blank'] += 1
                elif COMMENT5 in line.strip():
                    is_commnet = not is_commnet
                    result['comment'] += 1
                elif line.strip().startswith(COMMENT4) or is_commnet:
                    result['comment'] += 1
                else:
                    result['line'] += 1



def header():
    print '-----------------------------------------'
    print 'simple code statistics tools, v1.0. currenttly support C/C++, Java, Python, PHP'
    print ''

def print_res(dir, blank, comment, code, total):
    print '-----------------------------------------'
    print 'dir: %s' % dir
    print '-----------------------------------------'
    print 'blank|   comment|     code|   total|'
    print '%+8s| %+8s| %+8s|    %+8s|' % (blank, comment, code, total)
    print '-----------------------------------------'
 

if __name__ == '__main__':
    header()
    if len(sys.argv) != 2:
        print 'invalid args, type like this: python cal.py /path/to/dir'
        sys.exit()
    if not os.path.isdir(sys.argv[1]):
        print 'invalid dir, %s is not a dir, or the dir not exist!' % sys.argv[1]
        sys.exit()

    q = Queue.Queue()
    path = sys.argv[1]
    t1 = threading.Thread(target=crawl_files, args=(path, FILE_TYPE, thread_num, q))
    t2 = threading.Thread(target=calc_file, args=(q,))
    t1.start()
    t2.start()
    t2.join()

    print_res(path, result['blank'], result['comment'], result['line'], result['total'])
