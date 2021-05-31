# BOJ 17626
import sys

si = sys.stdin.readline

n = int(si())
dp = [5] * (n + 1)
for i in range(1, n + 1):
    if i ** 0.5 - int(i ** 0.5) == 0:
        dp[i] = 1
    else:
        for j in range(1, int(i ** 0.5) + 1):
            dp[i] = min(dp[i], dp[j ** 2] + dp[abs(i - j ** 2)])

print(dp[n])
