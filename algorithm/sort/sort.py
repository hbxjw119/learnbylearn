#encoding=utf-8

def bubble_sort(arr):
    """
    复杂度：best:O(n) avg:O(n^2) worst:O(n^2)
    """
    l = len(arr)
    for i in range(1,l):
        for j in range(0,l - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1]  = arr[j + 1] , arr[j]

    return arr


def select_sort(arr):
    """
    复杂度：best:O(n^2) avg:O(n^2) worst:O(n^2)
    """
    l = len(arr)
    for i in range(l-1):
        index = i
        tmp = arr[i]
        for j in range(i+1,l):
            if tmp > arr[j]:
                tmp = arr[j]
                index = j

        arr[i],arr[index] = arr[index],arr[i]

    return arr


def insert_sort(arr):
    """
    复杂度：best:O(n) avg:O(n^2) worst:O(n^2)
    """
    l = len(arr)
    for i in range(l):
        cur = arr[i]
        preIndex = i - 1
        while preIndex >= 0 and arr[preIndex] > cur:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = cur
    return arr


def merge_sort(arr):
    """
    复杂度：best:O(nlgn) avg:O(nlgn) worst:O(nlgn)
    空间复杂度：O(n)
    """
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left,right)

def _merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left
    if right:
        result += right

    return result

def _partition(arr,start,end):
    wall = start
    pivot = arr[end] #last is the pivot
    for i in range(start,end):
        if arr[i] < pivot:
            arr[i],arr[wall] = arr[wall],arr[i]
            wall += 1
    arr[wall],arr[end] = arr[end],arr[wall]
    return wall

def qsort(arr,start,end):
    """
    复杂度：best:O(n) avg:O(nlgn) worst:O(n^2)
    """
    if start < end:
        pos = _partition(arr,start,end)

        qsort(arr,start,pos - 1)
        qsort(arr,pos + 1, end)

        return arr

def qsort2(arr):
    if len(arr) <= 1:
        return arr

    left = [i for i in arr[1:] if i < arr]
    right = [i for i in arr[1:] if i >= arr]

    return qsort2(left) + [arr[0]] + qsort2(right)

if __name__ == '__main__':
    import random
    l = [i for i in range(10)]
    random.shuffle(l)

    print 'before sort:',l
    print 'bubble_sort:',bubble_sort(l)
    print 'select_sort:',select_sort(l)
    print 'insert_sort:',insert_sort(l)
    print 'merge_sort:',merge_sort(l)
    print 'qsort:',qsort(l,0,len(l)-1)

