# BOJ 2412 암벽 등반
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def bfs(locations):
    que = deque()
    visited = [False] * N
    que.append((0, 0, 0))  # y, x, cnt
    while que:
        y, x, cnt = que.popleft()

        if y == T:
            return cnt

        for i in range(N):
            ny, nx = locations[i]
            if abs(ny - y) > 2 or abs(nx - x) > 2:
                continue
            if not visited[i]:
                visited[i] = True
                que.append((ny, nx, cnt + 1))
    return -1


N, T = map(int, si().split(" "))

locations = []
for _ in range(N):
    a, b = map(int, si().split(" "))
    locations.append((b, a))  # y, x
print(bfs(locations))
