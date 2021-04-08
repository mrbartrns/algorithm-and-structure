# BOJ 9251
import sys

si = sys.stdin.readline

seq_a = si().strip()
seq_b = si().strip()
dp = [[0 for _ in range(len(seq_a) + 1)] for _ in range(len(seq_b) + 1)]
for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if seq_b[i - 1] == seq_a[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(dp) - 1][len(dp[0]) - 1])
