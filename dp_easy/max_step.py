# BOJ 2579번
import sys

input = sys.stdin.readline


def solve(n):
    memo[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, n):
        memo[i] = max(
            memo[i - 2] + stairs[i],
            memo[i - 3] + stairs[i - 1] + stairs[i],
        )
    return memo[-1]


"""
n = 6
stairs = [10, 20, 15, 25, 10, 20]
memo = [0] * n
memo[0] = stairs[0]
memo[1] = stairs[0] + stairs[1]
solve(n)
"""
n = int(input())
stairs = []
for i in range(n):
    stair = int(input())
    stairs.append(stair)
memo = [0] * n
memo[0] = stairs[0]
if n > 1:
    memo[1] = memo[0] + stairs[1]
print(solve(n) if n > 2 else memo[-1])
