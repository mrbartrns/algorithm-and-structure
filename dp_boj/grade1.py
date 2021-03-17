# BOJ 5557
import sys

sys.setrecursionlimit(3000)
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
dp = [[-1 for _ in range(21)] for _ in range(n)]

# x: idx, y: number(sum)
def dfs(x, y):
    if dp[x][y] > -1:
        return dp[x][y]

    if x == n - 1 and y == arr[n - 1]:
        dp[x][y] = 1
        return dp[x][y]

    dp[x][y] = 0
    if x + 1 < n and y - arr[x] >= 0:
        dp[x][y] += dfs(x + 1, y - arr[x])
    if x + 1 < n and y + arr[x] <= 20:
        dp[x][y] += dfs(x + 1, y + arr[x])
    return dp[x][y]


# 0, 0에서 시작하면 안되는 이유?
print(dfs(1, arr[0]))
