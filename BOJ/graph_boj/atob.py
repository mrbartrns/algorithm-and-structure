# BOJ 16953
import sys
from collections import deque

si = sys.stdin.readline


def bfs(a, b):
    que = deque()
    que.append((a, 1))
    visited.add(a)
    while que:
        v, cnt = que.popleft()
        if v == b:
            return cnt
        if 2 * v not in visited and 2 * v <= b:
            visited.add(2 * v)
            que.append((2 * v, cnt + 1))
        if 10 * v + 1 not in visited and 10 * v + 1 <= b:
            visited.add(10 * v + 1)
            que.append((10 * v + 1, cnt + 1))
    return -1


visited = set()
n, m = map(int, si().split())
print(bfs(n, m))
