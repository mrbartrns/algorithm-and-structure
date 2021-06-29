# 1로 만들기
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321


# memoization
def divide(n):
    if n == 1:
        return 0

    if dp[n] < INF:
        return dp[n]

    dp[n] = divide(n - 1) + 1
    if n % 2 == 0:
        dp[n] = min(dp[n], divide(n // 2) + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], divide(n // 3) + 1)
    if n % 5 == 0:
        dp[n] = min(dp[n], divide(n // 5) + 1)
    return dp[n]


n = int(si())
dp = [0] * 30001
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
print(dp[n])
