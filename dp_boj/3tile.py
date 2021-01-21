# BOJ 2133번
import sys

input = sys.stdin.readline

"""
def solve(n):
    if n >= 2:
        memo[2] = 3

    if n % 2 == 0:
        for i in range(4, n + 1, 2):
            memo[i] = memo[i - 2] * memo[2]
            for j in range(4, i, 2):
                memo[i] += memo[i - j] * 2
            memo[i] += 2
    return memo[n]
"""


def solve(n):
    if n >= 2:
        memo[2] = 3

    for i in range(4, n + 1, 2):
        memo[i] = 3 * memo[i - 2] + sum(memo[: i - 4 + 1]) * 2
    return memo[n]


n = int(input())
memo = [0] * (n + 1)
memo[0] = 1


print(solve(n))