# BOJ 2410 2의 멱수
# 배열을 뒤집으면 왜 결과가 달라지는지 파악하기
import sys


sys.setrecursionlimit(1000000)
si = sys.stdin.readline
MOD = 1000000000


def solve(k, p):
    if p == 0 or k == 0:
        dp[k][p] = 1
        return dp[k][p]
    if dp[k][p] > 0:
        return dp[k][p]
    s = 0
    for i in range(p + 1):
        if k - (1 << i) >= 0:
            s += solve(k - (1 << i), i)
            s %= MOD
        else:
            break
    dp[k][p] = s
    return dp[k][p]


dp = [[0 for _ in range(21)] for _ in range(1000001)]
N = int(si())
print(solve(N, 20))
