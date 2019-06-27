#encoding=utf-8

from Node import Node
import random

def create_list():
    head = None
    cur = None

    for _ in range(6):
        x = random.randint(1,10)
        cur = Node(x)
        cur.next = head
        head = cur
    return head