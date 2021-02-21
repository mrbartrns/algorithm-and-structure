# BOJ 2011
import sys

si = sys.stdin.readline

pw = si().strip()
mod = 1000000


def solve(pw):
    dp = [0] * 5001
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(pw) + 1):
        if pw[i - 1] > "0":
            dp[i] = dp[i - 1] % mod
        n = int(pw[i - 1]) + int(pw[i - 2]) * 10
        if 10 <= n and n <= 26:
            dp[i] = (dp[i] + dp[i - 2]) % mod
    return dp[len(pw)]


if pw[0] == "0":
    print(0)
    sys.exit(0)
else:
    print(solve(pw))