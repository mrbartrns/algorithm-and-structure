# BOJ 9251
import sys

si = sys.stdin.readline

"""
ACAYKP
CAPCAK
두개의 수열 모두에 대해 실행?
어떤 한개의 수열을 순회하면서 그 문자가 다른수열의 현재 인덱스보다 작거나 같은 위치에 있는지 실행
"""

a = si().strip()
b = si().strip()


def solve(a, b):
    n = len(a)
    m = len(b)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[n][m]  # 여기서 인덱스에러 발생했었음


print(solve(a, b))