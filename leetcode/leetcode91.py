#!/usr/bin/python

def num_decode(s):
    sl = len(s)
    dp = [0] * (sl + 1)
    dp[0] = 1
    for i in range(1, len(dp)):
        if s[i-1] == '0':
            dp[i-1] = 0
        if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] < '7'):
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]
    return dp

if __name__ == '__main__':
    l = num_decode('22105')
    print l
