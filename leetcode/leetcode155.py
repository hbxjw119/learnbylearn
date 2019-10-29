#!/usr/bin/python

class MinStack(object):
    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x):
        self.a.append(x)
        if len(self.b) == 0:
            self.b.append(x)
        else:
            if x < self.b[-1]:
                self.b.append(x)
            else:
                self.b.append(self.b[-1])

    def pop(self):
        if len(self.a) == 0:
            raise Exception("stack is empty")

        self.a.pop(-1)
        self.b.pop(-1)

    def getMin(self):
        return self.b[-1]

    def top(self):
        return self.a[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print minStack.getMin()
    minStack.pop()
    print minStack.top()
    print minStack.getMin()
