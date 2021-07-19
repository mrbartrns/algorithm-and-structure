import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def solve(idx):
    if idx > n:
        return 0

    if dp[idx] > -1:
        return dp[idx]

    dp[idx] = 0
    if idx + t[idx] <= n + 1:
        dp[idx] = solve(idx + t[idx]) + arr[idx]
    dp[idx] = max(dp[idx], solve(idx + 1))
    return dp[idx]


n = int(si())
t = [0] * (n + 1)
arr = [0] * (n + 1)
for i in range(1, n + 1):
    a, b = map(int, si().split())
    t[i] = a
    arr[i] = b

dp = [-1] * 21
print(solve(1))
# print(dp)
