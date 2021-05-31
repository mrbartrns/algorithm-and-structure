# 부분 문자열 다루기
import sys

si = sys.stdin.readline


def solve(s):
    max_length = 0
    for i in range(n):
        dp[i][i] = int(s[i])

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1  # 총 길이
            k = length // 2
            dp[i][j] = dp[i][j - k] + dp[j - k + 1][j]

            if length % 2 == 0 and dp[i][j - k] == dp[j - k + 1][j]:
                max_length = max(max_length, length)
    return max_length


n = 7
s = "9430723"
dp = [[0 for _ in range(n)] for _ in range(n)]
print(solve(s))

