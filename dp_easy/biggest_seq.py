# BOJ 11055 가장 긴 증가하는 부분 수열
import sys

input = sys.stdin.readline


def solve(n):
    for i in range(1, n):
        flag = False
        for j in range(i):
            if sequence[i] > sequence[j]:
                flag = True
                memo[i] = max(memo[i], sequence[i] + memo[j])
        if not flag:
            memo[i] = sequence[i]
    return max(memo)


"""
n = 10
sequence = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8]
memo = [0] * n
memo[0] = sequence[0]
print(solve(n))
"""
n = 5
sequence = [10, 90, 20, 80, 100]
memo = [0] * n
memo[0] = sequence[0]
print(solve(n))
"""
n = int(input())
sequence = list(map(int, input().split()))
memo = [0] * n
memo[0] = sequence[0]
print(solve(n))
"""