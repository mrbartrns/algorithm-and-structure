# BOJ 11726 tiling
import sys

# sys.setrecursionlimit()필요
def solve_recur(n):
    if n <= 1:
        return memo[n]

    if memo[n] > 1:
        return memo[n]

    memo[n] = (solve(n - 1) + solve(n - 2)) % 10007
    return memo[n]


def solve(n):
    if n >= 2:
        for i in range(2, n + 1):
            memo[i] = (memo[i - 1] + memo[i - 2]) % 10007
    return memo[n]


n = int(sys.stdin.readline())
memo = [1] * (n + 1)
sys.stdout.write(str(solve(n)))