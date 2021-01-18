import sys

input = sys.stdin.readline


# initiate


def solve(n):
    for i in range(99):
        for j in range(10):
            if j >= 1:  # 두번째부터 각 항을 더한다
                dp[i + 1][j - 1] += dp[i][j]
            if j < 9:
                dp[i + 1][j + 1] += dp[i][j]
    value = (sum(dp[n - 1])) % 1000000000
    return value


n = int(input())
dp = [[0 for _ in range(10)] for _ in range(100)]
for i in range(1, len(dp[0])):
    dp[0][i] = 1
# print(dp[0])
print(solve(n))