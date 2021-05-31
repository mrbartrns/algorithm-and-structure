# BOJ 11053번 가장 긴 증가하는 부분수열
import sys

input = sys.stdin.readline


def solve(n):
    for i in range(1, n):
        for j in range(i):
            if sequence[j] < sequence[i]:
                memo[i] = max(memo[i], memo[j] + 1)
    return max(memo)


n = int(input())
sequence = list(map(int, input().split()))
memo = [1] * n
print(solve(n))