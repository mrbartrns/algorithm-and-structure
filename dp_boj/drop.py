# BOJ 14501
import sys

si = sys.stdin.readline


def solve(n):
    dp = [0] * n

    for i in range(0, n):
        if t[i] <= n:
            dp[i] = arr[i]

        for j in range(i):
            if t[j] <= i:
                dp[i] = max(dp[i], dp[j] + arr[i])
            else:
                dp[i] = max(dp[i], dp[j])

    return dp


"""
n = int(si())
t = [i for i in range(n)]
arr = [0] * n

for i in range(n):
    u, v = map(int, si().split())
    t[i] += u
    arr[i] = v
"""

n = 7
t = [3, 6, 3, 4, 6, 9, 8]
arr = [10, 20, 10, 20, 15, 40, 200]

print(solve(n))