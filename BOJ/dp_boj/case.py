# BOJ 14494 다이나믹이 뭐에요?
import sys

sys.setrecursionlimit(1000000)
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
MOD = 1000000007


def memoize(y, x):
    if dp[y][x] > -1:
        return dp[y][x]

    if y == n and x == m:
        dp[y][x] = 1
        return dp[y][x]

    dp[y][x] = 0
    if y + 1 <= n:
        dp[y][x] += memoize(y + 1, x) % MOD
    if x + 1 <= m:
        dp[y][x] += memoize(y, x + 1) % MOD
    if y + 1 <= n and x + 1 <= m:
        dp[y][x] += memoize(y + 1, x + 1) % MOD
    dp[y][x] = dp[y][x] % MOD
    return dp[y][x]


n, m = map(int, si().split(" "))
dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
print(memoize(1, 1))