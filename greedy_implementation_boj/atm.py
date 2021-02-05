# BOJ 11399
import sys

si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
# arr = [3, 1, 4, 3, 2]  # 1 2 3 3 4
# n = 5
arr.sort()


def solve(arr):
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = arr[i] + dp[i - 1]
    return sum(dp)


print(solve(arr))
"""
N = int(input())

L = list(map(int, input().split()))

L.sort()

sum = 0
for i in range(N):
    sum += L[i]*(N-i)

print(sum)
N - i 가 무슨의미?
"""