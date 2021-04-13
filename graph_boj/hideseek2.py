# BOJ 12851
import sys
from collections import deque

si = sys.stdin.readline


def bfs(start, end):
    que = deque()
    que.append((start, 0))
    res = 0
    while que:
        v, cnt = que.popleft()
        visited[v] = True
        if v == end:
            res += 1
            ans = cnt
            while que:
                u, cnt = que.popleft()
                if u == end and ans == cnt:
                    res += 1
            return ans, res
        if v < end:
            if not visited[2 * v]:
                que.append((2 * v, cnt + 1))
            if not visited[v + 1]:
                que.append((v + 1, cnt + 1))
        if v - 1 >= 0 and not visited[v - 1]:
            que.append((v - 1, cnt + 1))


visited = [False] * 200001
s, e = map(int, si().split())
cnt, cases = bfs(s, e)
print(cnt)
print(cases)
