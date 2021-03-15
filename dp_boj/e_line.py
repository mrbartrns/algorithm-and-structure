# BOJ 2565
import sys

si = sys.stdin.readline


def solve(n):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i][1] > arr[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


arr = []
n = int(si())
for _ in range(n):
    a, b = map(int, si().split())
    arr.append((a, b))

arr.sort(key=lambda x: x[0])


val = n - solve(n)
print(val)

"""
n = 8

arr = [(1, 8), (3, 9), (2, 2), (4, 1), (6, 4), (10, 10), (9, 7), (7, 6)]
"""
