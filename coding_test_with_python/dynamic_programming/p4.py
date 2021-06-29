# 효율적인 화폐 구성
"""
메모이제이션으로 바꾼 후 생각해보기
"""
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321

n, m = map(int, si().split())
coins = [int(si()) for _ in range(n)]
dp = [INF for _ in range(10001)]

for i in range(n):
    for j in range(m + 1):
        if m % coins[i] == 0:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)
print(dp[m] if dp[m] < INF else -1)
