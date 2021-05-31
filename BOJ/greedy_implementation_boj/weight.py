# BOJ 2437
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
arr.sort()
res = set()


# dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# for i in range(1, n + 1):
#     dp[i][i] = arr[i]
#
# for i in range(n, 0, -1):
#     for j in range(i + 1, n + 1):
#         dp[i][j] = dp[i][j - 1] + arr[j]
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         res.add(dp[i][j])
#
# for i in range(n + 1):
#     print(dp[i])

def solve(s, idx):
    if idx == n:
        res.add(s)
        return
    solve(s + arr[idx], idx + 1)
    solve(s, idx + 1)


solve(0, 0)
print(res)
