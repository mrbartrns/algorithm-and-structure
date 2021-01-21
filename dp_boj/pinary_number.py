# BOJ 2193
import sys

input = sys.stdin.readline


def solve(n):
    for i in range(1, n):
        memo[i][0] = memo[i - 1][0] + memo[i - 1][1]
        memo[i][1] = memo[i - 1][0]
    return sum(memo[n - 1])


n = int(input())
memo = [[0, 0] for _ in range(n)]
memo[0][1] = 1
print(solve(n))