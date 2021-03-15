# BOJ 2565
import sys

si = sys.stdin.readline

n = int(si())
arr = []
for _ in range(n):
    a, b = map(int, si().split())
    arr.append((a, b))

arr.sort(key=lambda x: x[0])


def solve(n):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i][1] > arr[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


print(n - solve(n))