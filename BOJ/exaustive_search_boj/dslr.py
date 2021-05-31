# BOJ 9019
import sys
from collections import deque

si = sys.stdin.readline


def bfs(n, m):
    que = deque([(n, "")])
    visited.add(n)
    while que:
        v, prompt = que.popleft()
        if v == m:
            return prompt

        # case 'D'
        d = (v * 2) % 10000
        if d not in visited:
            visited.add(d)
            que.append((d, prompt + "D"))

        # case 'S'
        s = v - 1 if v > 0 else 9999
        if s not in visited:
            visited.add(s)
            que.append((s, prompt + "S"))

        # case 'L'
        l = (v * 10) % 10000 + v // 1000
        if l not in visited:
            visited.add(l)
            que.append((l, prompt + "L"))

        # case 'R'
        r = (v % 10) * 1000 + v // 10
        if r not in visited:
            visited.add(r)
            que.append((r, prompt + "R"))
    return None


t = int(si())
for _ in range(t):
    n, m = map(int, si().split())
    visited = set()
    sys.stdout.write(bfs(n, m) + "\n")
