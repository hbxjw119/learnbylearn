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

if __name__ == '__main__':
    queen(0)