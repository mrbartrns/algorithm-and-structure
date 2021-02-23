# BOJ 2186
import sys

si = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[[-1 for _ in range(81)] for _ in range(100)] for _ in range(100)]


def dfs(x, y, idx):
    if dp[x][y][idx] > -1:
        return dp[x][y][idx]

    if idx >= len(word):
        return 1

    dp[x][y][idx] = 0
    for i in range(4):
        for j in range(1, k + 1):
            nx = x + dx[i] * j
            ny = y + dy[i] * j
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 위에서 따로 걸러내는 종결조건이 없으므로 for문을 돌때 해결해야함
            if puzzle[nx][ny] != word[idx]:
                continue
            dp[x][y][idx] += dfs(nx, ny, idx + 1)
    return dp[x][y][idx]


n, m, k = map(int, si().split())
puzzle = []
for _ in range(n):
    puzzle.append(list(si().strip()))

word = si().strip()


"""
n, m, k = 4, 4, 1
puzzle = [
    ["K", "A", "K", "T"],
    ["X", "E", "A", "S"],
    ["Y", "R", "W", "U"],
    ["Z", "B", "Q", "P"],
]
word = "BREAK"
"""
res = 0
for i in range(n):
    for j in range(m):
        if word[0] == puzzle[i][j]:
            res += dfs(i, j, 1)
print(res)
