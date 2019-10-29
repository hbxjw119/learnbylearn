#encoding=utf-8

Q = [None] * 8

def confict(n):
    global Q
    for i in range(n):
        if Q[i] == Q[n] or abs(n - i) == abs(Q[n] - Q[i]):
            return True
    return False

def queen(n):
    global qc
    if n == 8:
        print Q
        return
    for i in range(8):
        Q[n] = i
        if not confict(n):
            queen(n + 1)


def valid_str(s):
    l = '({['
    r = ')}]'
    t = []
    for i in s:
        if i in l:
            t.append(i)
        else:
            if len(t) == 0:
                return False
            a = t.pop()
            if l.index(a) != r.index(i):
                return False
    return len(t) == 0


def longest_com_pre(s):
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s[0]
    l = len(s[0])
    t = s[0]
    for i in s:
        if len(i) < l:
            l = len(i)
            t = i

    for j in range(len(t)):
        for k in s:
            if k[j] == t[j]:
                continue
            else:
                return t[:j]


    return t


def reverse_num(x):
    if x == 0:
        return 0
    t = str(x)[::-1].lstrip('0').rstrip('-')
    t = int(t) if x > 0 else -int(t)

    if -2**31 < t < 2**31-1:
        return t
    else:
        return 0

def search_insert(nums, target):
    l = len(nums)
    if l == 0 or nums[0] > target:
        return 0

    for i in range(l):
        if nums[i] < target:
            continue

        if nums[i] >= target:
            return i

    return l


def max_uniq(s):
    if not s:
        return ''

    _len = 0
    t = ''
    m = ''
    for i in s:
        if i not in t:
            t += i
            _len = max(_len, len(t))
            idx = s.index(i) - _len

            tmp = s[idx+1:s.index(i)+1]
            if len(tmp) > len(m):
                m = tmp

        else:

            t += i
            t = t[t.index(i) + 1:]

    return _len
    #return m


if __name__ == '__main__':
    #print max_uniq("abcabcbb")
    print search_insert([1,3,5,6], 5)
    print search_insert([1,3,5,6], 2)
    print search_insert([1,3,5,6], 7)
    print search_insert([1,3,5,6], 0)
    print search_insert([], 0)
