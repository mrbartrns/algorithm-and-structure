# BOJ 9019
import sys
from collections import deque

si = sys.stdin.readline


def bfs(s, e):
    que = deque([(s, "")])
    visited.add(s)
    while que:
        n, prompt = que.popleft()

        if n == e:
            return prompt

        # D
        num = (n * 2) % 10000
        if num not in visited:
            visited.add(num)
            que.append((num, prompt + "D"))

        # S
        num = n - 1 if n > 0 else 9999
        if num not in visited:
            visited.add(num)
            que.append((num, prompt + "S"))

        # L
        num = (n // 1000) + ((n % 1000) * 10)
        if num not in visited:
            visited.add(num)
            que.append((num, prompt + "L"))

        # R
        num = (n % 10) * 1000 + (n // 10)
        if num not in visited:
            visited.add(num)
            que.append((num, prompt + "R"))


t = int(si())
for _ in range(t):
    s, e = map(int, si().split())
    visited = set()
    print(bfs(s, e))