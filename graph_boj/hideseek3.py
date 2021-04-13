# BOJ 13549
import sys
from collections import deque

si = sys.stdin.readline


def bfs(s, t):
    que = deque()
    que.append((s, 0))
    while que:
        s, cnt = que.popleft()
        visited[s] = True
        if s == t:
            res = cnt
            while que:
                s, cnt = que.popleft()
                if s == t:
                    res = min(res, cnt)
            return res
        if s < t:
            if not visited[2 * s]:
                que.append((2 * s, cnt))
            if not visited[s + 1]:
                que.append((s + 1, cnt + 1))
        if s - 1 >= 0 and not visited[s - 1]:
            que.append((s - 1, cnt + 1))


s, t = map(int, si().split())
visited = [False] * 200001

print(bfs(s, t))
