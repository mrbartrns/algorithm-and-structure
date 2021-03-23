# BOJ 11866
# 다시 볼것
import sys
from collections import deque

si = sys.stdin.readline

n, k = map(int, si().split())
que = deque([i for i in range(1, n + 1)])
arr = []
idx = 1
while que:
    el = que.popleft()
    if idx == k:
        idx = 1
        arr.append(el)
    else:
        idx += 1
        que.append(el)

string = "<"
string += ", ".join(list(map(str, arr)))
string += ">"
print(string)