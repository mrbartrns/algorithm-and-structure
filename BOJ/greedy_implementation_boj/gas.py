# BOJ 3109 빵집

import sys

# sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def solve(y, x):
    if dp[y][x] > -1:
        return 0

    if x == C - 1:
        dp[y][x] = 1
        return dp[y][x]

    dp[y][x] = 0
    if graph[y][x + 1] != "x":
        dp[y][x] = max(dp[y][x], solve(y, x + 1))
    if y - 1 >= 0 and graph[y - 1][x + 1] != "x":
        dp[y][x] = max(dp[y][x], solve(y - 1, x + 1))
    if y + 1 < R and graph[y + 1][x + 1] != "x":
        dp[y][x] = max(dp[y][x], solve(y + 1, x + 1))
    return dp[y][x]


# R, C = map(int, si().split())
# graph = [list(si().strip()) for _ in range(R)]
R, C = 5, 5
graph = [
    [".", "x", "x", ".", "."],
    [".", ".", "x", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", "x", "."],
    [".", ".", ".", "x", "."],
]
dp = [[-1 for _ in range(C)] for _ in range(R)]
solve(0, 0)
for i in range(R):
    for j in range(C):
        print(dp[i][j], end=" ")
    print()