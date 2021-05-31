# BOJ 2447
import sys

si = sys.stdin.readline

n = int(si())

graph = [[" " for _ in range(n)] for _ in range(n)]


def solve(x, y, k):
    if k == 1:
        graph[x][y] = "*"
        return

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            solve(x + i * (k // 3), y + j * (k // 3), k // 3)


solve(0, 0, n)
for i in range(n):
    print("".join(graph[i]))