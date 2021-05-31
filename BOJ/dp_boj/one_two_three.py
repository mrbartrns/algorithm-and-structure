import sys


def solve(n):
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    if n < 2:
        print(1)
    else:
        memo = [0] * (n + 1)
        memo[0] = memo[1] = 1
        memo[2] = 2
        print(solve(n))