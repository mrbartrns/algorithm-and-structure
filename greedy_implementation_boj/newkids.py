# BOJ 11497
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

t = int(si())
for _ in range(t):
    n = int(si())
    arr = list(map(int, si().split()))
    arr.sort()
    que = deque()
    val = 0
    while arr:
        el = arr.pop()
        que.appendleft(el)
        if arr:
            el = arr.pop()
            que.append(el)
        val = max(abs(que[0] - que[1]), abs(que[-1] - que[-2]), val)
    print(val)
