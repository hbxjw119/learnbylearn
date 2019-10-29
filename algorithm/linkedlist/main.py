#encoding=utf-8

import create
import Node

def merge_two_list(l1, l2):
    idx = Node.Node(-1)
    head = idx
    while l1 and l2:
        if l1.val < l2.val:
            idx.next = l1
            l1 = l1.next
            idx = idx.next
        else:
            idx.next = l2
            l2 = l2.next
            idx = idx.next
    if l1:
        idx.next = l1
    if l2:
        idx.next = l2

    return head.next

def remove_nth_from_end(head, n):
    a = head
    for _ in range(n):
        a = a.next

    if not a:
        return head.next
    b = head
    pre = None

    while a:
        pre = b
        a = a.next
        b = b.next
    pre.next = b.next

    return head


def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'

    f = 0
    res = ''
    s = []
    while num2:
        x = int(num2[-1])
        t = num1
        f = 0
        while t:
            y = int(t[-1])
            r = int(x) * int(y)
            i = r % 10
            m = r // 10

            res = str(i + f) + res

            f = m

            t = t[:-1]
        s.append(res)
        res = ''

        num2 = num2[:-1]
    return s



def my_pow(x, n):

    if n == 0:
        return 1

    if n < 0:
        return 1 / my_pow(x, -n)
    y = my_pow(x, n / 2)
    if (n % 2 != 0):
        return y * y * x

    return y * y

def is_palindrome(s):
    if not s:
        return True

    s = s.lower()
    l = 0
    r = len(s) - 1
    while l <= r:
        ll = s[l]
        rr = s[r]
        if not ll.isalpha() and not ll.isdigit():
            l += 1
            continue
        if not rr.isalpha() and not rr.isdigit():
            r -= 1
            continue
        if ll != rr:
            return False
        l += 1
        r -= 1
    return True



def rotate_right(head, k):
    if head is None or head.next is None:
        return head
    idx = head
    l = 0
    while idx:
        l += 1
        idx = idx.next
    if k % l == 0:
        return head
    k = k % l
    idx = head

    for i in range(k):
        idx = idx.next
        if idx is None:
            idx = head

    nxt = idx.next
    if nxt is None:
        return head
    new_head = nxt

    while nxt and nxt.next is not None:
        nxt = nxt.next

    nxt.next = head
    idx.next = None
    return new_head

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    h = head
    n = head.next
    h.next = swap_pairs(n.next)
    n.next = h
    return n

def delete_duplicate(head):
    if head is None or head.next is None:
        return head
    idx = head
    du = Node.Node(0)
    import collections

    d = collections.OrderedDict()
    while idx:
        if idx.val in d:
            d[idx.val] += 1
        else:
            d[idx.val] = 1
        idx = idx.next

    h = du
    for k,v in d.iteritems():
        if v == 1:
            du.next = Node.Node(k)
            du = du.next

    return h.next

def delete_duplicate2(head):
    if head is None or head.next is None:
        return head
    idx = head
    du = Node.Node(-1)
    pre = du
    du.next = idx
    while idx:
        if pre.val != idx.val:
            pre = pre.next
            idx = idx.next
        else:
            pre.next = idx.next
            idx = idx.next
    return head

def min_path_sum(grid):
    res = []
    l1 = grid[0]
    col = len(l1)
    row = len(grid)
    for i in range(row):
        t = [0] * col
        for j in range(col):
            if j == 0 and i == 0:
                t[j] = grid[i][j]
            else:
                if i == 0:
                    t[j] = t[j-1] + grid[i][j]
                elif j == 0:
                    t[j] = res[i-1][0] + grid[i][j]
        res.append(t)


    for i in range(1, row):
        for j in range(1, col):
            res[i][j] = min(res[i-1][j] + grid[i][j] , res[i][j-1] + grid[i][j])
    print res
    return res[-1][-1]


def simplify_path(path):
    res = ''
    if not path:
        return '/'

    l = path.split("/")
    l = list(filter(lambda x: x!='', l))
    res += '/'
    t = []
    for i in l:
        if i == '.':
            continue
        if i == '..':
            if len(t) != 0:
                t.pop()
            else:
                t = []
        else:
            t.append(i)

    res = res + '/'.join(t)
    return res

def merge_field(intervals):
    res = []
    l = len(intervals)
    intervals = sorted(intervals, key=lambda k: (k[0],k[1]))
    i = 0
    while l > 1 and i < l-1:
        if intervals[i][1] >= intervals[i+1][0]:
            b = min(intervals[i][0], intervals[i+1][0])
            e = max(intervals[i+1][1], intervals[i][1])
            intervals.pop(i)
            intervals.pop(i)
            intervals.insert(i, [b,e])
            l = len(intervals)
            i = 0
            continue
        else:
            i +=1


    return intervals

def reverse_between(head, m, n):

    if head is None or head.next is None:
        return head
    pre = Node.Node(0)
    pre.next = head
    tt = m
    c = None
    while tt:
        c = pre
        pre = pre.next
        tt -= 1

    b = c

    l =[]
    k = b.next
    for i in range(m, n+1):
        l.append(k)
        k = k.next

    e = k

    a = b
    t = b
    while l:
        b = t
        b.next = l.pop()
        t = b.next

    t.next = e

    return a.next


def _partition(head, x):
    l = Node.Node(0)
    r = Node.Node(0)

    a, b = l ,r

    while head:
        if head.val < x:
            a.next = head
            a = a.next
        else:
            b.next = head
            b = b.next
        head = head.next
    b.next = None
    a.next = r.next

    return l.next


def add_two_num(l1, l2):
    a, b = l1, l2
    s1, s2 = [], []
    r = []
    s = Node.Node(0)
    h = s
    f = 0
    while a:
        s1.append(a)
        a = a.next
    while b:
        s2.append(b)
        b = b.next
    while s1 and s2:
        t = s1.pop().val+ s2.pop().val
        i = (t + f) % 10
        f = (t + f) // 10
        m = Node.Node(i)
        r.append(m)

    while s1:
        t = s1.pop().val
        i = (t + f) % 10
        f = (t + f) // 10
        m = Node.Node(i)
        r.append(m)
    while s2:
        t = s2.pop().val
        i = (t + f) % 10
        f = (t + f) // 10
        m = Node.Node(i)
        r.append(m)
    if f:
        m = Node.Node(f)
        r.append(m)

    r.reverse()
    for i in r:
        s.next = i
        s = s.next
    return h.next






def combination_sum(candidates, target):
    def find(output, target):
        if target == 0 and sorted(output) not in res:
            res.append(sorted(output))
            return
        for candidate in candidates:
            new_target = target - candidate
            if new_target >= 0:
                find(output + [candidate], new_target)

    res = []
    find([], target)
    return res


def get_intersection_node(head_a, head_b):
    if head_a is None or head_b is None:
        return None

    a, b = head_a, head_b
    l_a = l_b = 0
    while a:
        l_a += 1
        a = a.next
    while b:
        l_b += 1
        b = b.next
    t = 0
    n = None
    if l_a > l_b:
        t = l_a - l_b
        while t:
            head_a = head_a.next
            t -= 1
    else:
        t = l_b - l_a
        while t:
            head_b = head_b.next
            t -= 1

    while head_a != head_b:
        head_a = head_a.next
        head_b = head_b.next
        if head_a is None or head_b is None:
            return None


    return head_a







def sort_colors(nums):
    if not nums or len(nums) == 1:
        return nums
    b = 0
    e = len(nums) - 1

    index = 0
    while b <= e:
        if nums[b] == 0:
            nums[index], nums[b] = nums[b], nums[index]
            index += 1
            b += 1
        elif nums[b] == 2:
            nums[e], nums[b] = nums[b], nums[e]
            e -= 1
        else:
            b += 1

    return nums



def mid_reverse(root):
    res = []
    if root:
        mid_reverse(root.left)
        res.append(root.val)
        mid_reverse(root.right)

def mid_reverse2(root):
    res = []
    n = []
    cur = root
    while n or cur:
        if cur:
            n.append(cur)
            cur = cur.left
        else:
            cur = n.pop()
            res.append(cur.val)
            cur = cur.right
    return res

def sub_sets(nums):
    res = [[]]
    for i in range(len(nums)):
        l = len(res)
        for j in range(0, l):
            t = list(res[j])
            t.append(nums[i])
            res.append(t)

    return res

def _sqrt(x):
    if x in [0,1]:
        return x

    l, r = 0, x
    mid = 0
    while abs(l-r)> 1.0e-4:
        mid = l + (r - l) / 2.0
        if mid * mid > x:
            r = mid
        elif mid* mid == x:
            return int(mid)
        else:
            l = mid
    return mid


# 反转链表 递归
def reverse_list(head):
    if head is None or head.next is None:
        return head
    tmp_head = reverse_list(head.next)
    t1 = head.next
    t1.next = head
    head.next = None
    return tmp_head

# 反转链表 非递归
def reverse_list2(head):
    if head is None or head.next is None:
        return head
    cur = head
    tmp = None
    new_head = None

    while cur:
        tmp = cur.next
        cur.next = new_head
        new_head = cur
        cur = tmp
    return new_head

def _merge_sort(head):
    if head is None or head.next is None:
        return head

    fast = slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    l = head
    r = slow.next
    slow.next = None

    return _merge_two_list(_merge_sort(l), _merge_sort(r))


def _merge_two_list(l1, l2):
    d = Node.Node(0)
    res = d
    while l1 and l2:
        if l1.val < l2.val:
            res.next = l1
            res = res.next
            l1 = l1.next
        else:
            res.next = l2
            res = res.next
            l2 = l2.next
    if l1:
        res.next = l1
    if l2:
        res.next = l2

    return d.next


def reverse_k_group(head, k):
    if head is None or head.next is None or k <= 1:
        return head

    node = head
    dummy = Node.Node(0)
    dummy.next = head
    first = head
    last  = dummy
    cnt = 1
    while node:
        if cnt < k:
            cnt += 1
            node = node.next
        else:
            next_first = node.next
            last.next = reverse(first, node)
            last = first
            first.next = next_first
            node = first

            cnt = 1
    return dummy.next



# 链表归并排序

def sort_list(head):
    if head is None or head.next is None:
        return head

    mid = get_mid_node(head)
    right = mid.next
    mid.next = None

    return merge_list(sort_list(mid), sort_list(right))

def get_mid_node(head):
    if head is None or head.next is None:
        return head

    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 合并两个有序链表
def merge_list(head1, head2):
    p1 = head1
    p2 = head2
    while p1 and p2:
        if p1.val > p2.val:
            p = p2
            p2 = p2.next
        else:
            p = p1
            p1 = p1.next
        p = p.next
    if p1:
        p.next = p1
    if p2:
        p.next = p2
    return p


# 链表快排
def qsort_list(head):
    qsort(head, None)
    return

def qsort(head, end):
    if head == end or head.next == end:
        return

    p = partition(head, end)
    qsort(head, p)
    qsort(p.next, end)


def partition(begin, end):
    if begin == end or begin.next == end:
        return begin
    # 第一个为基准
    pivot = begin.val
    idx = begin
    cur = begin

    while cur != end:
        # 注意，只交换节点的值，而不是交换节点
        if cur.val < pivot:
            idx = idx.next
            t = cur.val
            cur.val = idx.val
            idx.val = t
        cur = cur.next
    m = idx.val
    idx.val = pivot
    begin.val = m
    return idx

if __name__ == '__main__':

    print is_palindrome("0P")


    head = create.create_list()
    t = Node.Node(4)
    t.next = Node.Node(3)
    t.next.next = Node.Node(5)
    t.next.next.next = Node.Node(9)
    l1 = t
    head = t
    h = head
    l = []
    while head:
        l.append(head.val)
        head = head.next
    print l

    i = remove_nth_from_end(t,4)
    k = []
    while i:
        k.append(i.val)
        i = i.next
    print k

    print '---------'

    b = Node.Node(2)
    b.next = Node.Node(4)
    p =[]
    r = _merge_sort(t)
    while r:
        p.append(r.val)
        r = r.next
    print p


    print '========='



    #t.next.next.next.next.next = Node.Node(2)

    t = Node.Node(2)
    t.next = Node.Node(4)
    t.next.next = Node.Node(8)
    t.next.next.next = l1.next
    head = t
    l2 = t
    h = head
    i = []
    while head:
        i.append(head.val)
        head = head.next
    print i

    m= get_intersection_node(l1, l2)
    if m is not None:
        print m.val
    else:
        print None

    r = merge_two_list(l1, None)
    i =[]
    while r:
        i.append(r.val)
        r = r.next
    print i



    print combination_sum([2,3,5],8)

    #a = _partition(h, 3)
    #while a:
    #    l2.append(a.val)
    #    a = a.next

    #print l2

    #print simplify_path("/a/./b/../../c/")
    #print simplify_path("/a/../../b/../c//.//")
    #print simplify_path("/a//b////c/d//././/..")
    #print simplify_path("/home/foo/.ssh/../.ssh2/authorized_keys/")
    #print simplify_path("/a/./b/../../c/")
    #print merge_field([[1,3],[2,6],[8,10],[15,18]])
    #print merge_field([[1,4],[4,5]])
    #print merge_field([[1,3],[2,6],[8,10],[15,18]])
    #print merge_field([[1,4],[0,4]])
    #print merge_field([[1,4],[0,1]])
    #print merge_field([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])
    #print sort_colors([2,0,1])



