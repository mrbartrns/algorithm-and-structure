# BOJ 1965
import sys

si = sys.stdin.readline


def solve(n):
    dp = [1] * n
    res = 1
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                res = max(dp[i], res)
    return res


n = int(si())
arr = list(map(int, si().split()))
print(solve(n))