# BOJ 2251
import sys
from collections import deque

si = sys.stdin.readline


def bfs(A, B, C):
    que = deque()
    que.append((0, 0))
    while que:
        a, b = que.popleft()
        c = C - a - b

        if visited[a][b]:
            continue

        visited[a][b] = True

        if a == 0:
            ans.append(c)

        # a -> b
        if a + b > B:
            que.append((a + b - B, B))
        else:
            que.append((0, a + b))

        # a -> c
        if a + c > C:
            que.append((a + c - C, b))
        else:
            que.append((0, b))

        # b -> a
        if b + a > A:
            que.append((A, b + a - A))
        else:
            que.append((a + b, 0))

        # b -> c
        if b + c > C:
            que.append((a, b + c - C))
        else:
            que.append((a, 0))

        # c -> a
        if c + a > A:
            que.append((A, b))
        else:
            que.append((a + c, b))

        # c -> b
        if c + b > B:
            que.append((a, B))
        else:
            que.append((a, b + c))


visited = [[False for _ in range(201)] for _ in range(201)]
ans = []
A, B, C = map(int, si().split())
bfs(A, B, C)
ans.sort()
sys.stdout.write(" ".join(map(str, ans)))