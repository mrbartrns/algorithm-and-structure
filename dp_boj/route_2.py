# BOJ 10164
import sys

si = sys.stdin.readline

move_dir = [(0, 1), (1, 0)]


def dfs(y, x, n, m) -> int:
    if dp[y][x] > -1:
        return dp[y][x]
    if y == n - 1 and x == m - 1:
        dp[y][x] = 1
        return dp[y][x]

    dp[y][x] = 0
    for i in range(2):
        dy, dx = move_dir[i]
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        dp[y][x] += dfs(ny, nx, n, m)
    return dp[y][x]


n, m, k = map(int, si().split())
dp = [[-1 for _ in range(m)] for _ in range(n)]
if k > 0:
    p, q = (k - 1) // m, (k - 1) % m
    s1 = dfs(0, 0, p + 1, q + 1)
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    s2 = dfs(p, q, n, m)
    print(s1 * s2)
else:
    print(dfs(0, 0, n, m))
