# BOJ 2447
import sys

si = sys.stdin.readline

n = int(si())
arr = [[" " for _ in range(n)] for _ in range(n)]


def solve(x, y, n):
    if n == 1:
        arr[x][y] = "*"
        return

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            solve(x + i * (n // 3), y + j * (n // 3), n // 3)


solve(0, 0, n)


for i in range(n):
    for j in range(n):
        print(arr[i][j], end="")
    print()
