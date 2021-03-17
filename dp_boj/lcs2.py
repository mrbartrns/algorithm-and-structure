# BOJ 9252
import sys

si = sys.stdin.readline

a = si().strip()
b = si().strip()
size_a = len(a)
size_b = len(b)

dp = [[0 for _ in range(size_a + 1)] for _ in range(size_b + 1)]
dp2 = [["" for _ in range(size_a + 1)] for _ in range(size_b + 1)]
for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if a[j - 1] == b[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            dp2[i][j] = dp2[i - 1][j - 1] + a[j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if dp[i - 1][j] > dp[i][j - 1]:
                dp2[i][j] = dp2[i - 1][j]
            else:
                dp2[i][j] = dp2[i][j - 1]
print(dp[size_b][size_a])
print(dp2[size_b][size_a])