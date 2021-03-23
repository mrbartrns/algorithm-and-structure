# BOJ 15829
import sys

si = sys.stdin.readline
r = 31
MOD = 1234567891

n = int(si())
string = si().strip()
dp = [0] * n
dp[0] = ord(string[0]) - ord("a") + 1
for i in range(1, n):
    dp[i] = (dp[i - 1] + (ord(string[i]) - ord("a") + 1) * (r ** i)) % MOD

print(dp[n - 1])
