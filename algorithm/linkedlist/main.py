#encoding=utf-8

import create

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

# 链表块排
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
    head = create.create_list()



