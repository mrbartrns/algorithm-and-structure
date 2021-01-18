# BOJ 11727
import sys


def solve(n):
    if n >= 2:
        for i in range(2, n + 1):
            memo[i] = (memo[i - 1] + memo[i - 2] * 2) % 10007
    return memo[n]


n = int(sys.stdin.readline())
memo = [1] * (n + 1)
sys.stdout.write(str(solve(n)))