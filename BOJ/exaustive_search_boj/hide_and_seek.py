# BOJ 1697
import sys
from collections import deque

si = sys.stdin.readline

n, m = map(int, si().split())

visited = [False] * 1000000
# DFS 사용 불가
# BFS 사용
def solve(n, m, visited):
    cnt = 0
    que = deque([n])
    visited[n] = True
    while que:
        size = len(que)
        for _ in range(size):
            v = que.popleft()
            if v == m:
                return cnt
            else:
                if v > m and not visited[v - 1]:
                    visited[v - 1] = True
                    que.append(v - 1)
                elif v < m:
                    if not visited[v - 1] and v - 1 >= 0:
                        visited[v - 1] = True
                        que.append(v - 1)
                    if not visited[v + 1]:
                        visited[v + 1] = True
                        que.append(v + 1)
                    if not visited[v * 2]:
                        visited[v * 2] = True
                        que.append(v * 2)
        cnt += 1


print(solve(n, m, visited))