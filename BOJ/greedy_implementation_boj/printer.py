# BOJ 1966
# 다시 복습할것
import sys
from collections import deque

si = sys.stdin.readline

t = int(si())


def solve(que, target):
    cnt = 1
    while que:
        v, idx = que.popleft()
        if not que or (v >= max(que)[0] and idx == target):
            return cnt
        if v >= max(que)[0]:
            cnt += 1
        else:
            que.append((v, idx))


for _ in range(t):
    n, idx = map(int, si().split())
    arr = list(map(int, si().split()))
    que = deque()
    for i in range(n):
        que.append((arr[i], i))
    print(solve(que, idx))