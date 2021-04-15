# BOJ 2133번
import sys

input = sys.stdin.readline

"""
def solve(n):
    if n >= 2:
        memo[2] = 3

    if n % 2 == 0:
        for y in range(4, n + 1, 2):
            memo[y] = memo[y - 2] * memo[2]
            for x in range(4, y, 2):
                memo[y] += memo[y - x] * 2
            memo[y] += 2
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