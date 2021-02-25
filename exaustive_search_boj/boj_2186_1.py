# BOJ 2186
# python3 미통과, pypy3 통과
import sys

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


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
            if graph[nx][ny] != word[idx]:
                continue
            dp[x][y][idx] += dfs(nx, ny, idx + 1)
    return dp[x][y][idx]


res = 0
dp = [[[-1 for _ in range(81)] for _ in range(100)] for _ in range(100)]
n, m, k = map(int, si().split())
graph = []
for _ in range(n):
    graph.append(list(si().strip()))
word = si().strip()

for i in range(n):
    for j in range(m):
        if graph[i][j] == word[0]:
            res += dfs(i, j, 1)

print(res)