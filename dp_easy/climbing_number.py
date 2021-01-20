# BOJ 11057번
import sys


input = sys.stdin.readline


def solve(n):
    for i in range(1, n):
        for j in range(10):
            memo[i][j] = (sum(memo[i - 1][j:])) % 10007
    return (sum(memo[n - 1])) % 10007


n = int(input())
memo = [[0 for _ in range(10)] for _ in range(n)]
for i in range(10):
    memo[0][i] = 1

print(solve(n))