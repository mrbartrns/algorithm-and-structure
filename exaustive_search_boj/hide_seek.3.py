# BOJ 13549
import sys
from collections import deque

si = sys.stdin.readline

s, t = map(int, si().split())
visited = [False] * (2 * t + 1)


def bfs(s, t):
    que = deque()
    que.append((s, 0))
    while que:
        s, cnt = que.popleft()
        visited[s] = True
        if s == t:
            return cnt
        if s < t:
            que.append((2 * s, cnt))
        if s - 1 >= 0:
            que.append((s - 1, cnt + 1))
        if s + 1 <= t:
            que.append((s + 1, cnt + 1))


print(bfs(s, t))
