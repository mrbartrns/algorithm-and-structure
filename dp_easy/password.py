# BOJ  2011


def solve(s):
    if s[0] == "0":
        return 0

    for i in range(2, len(s) + 1):
        if s[i - 1] > "0":
            dp[i] = dp[i - 1] % mod
        n = int(s[i - 1]) + int(s[i - 2]) * 10
        if n >= 10 and n <= 26:
            dp[i] = (dp[i] + dp[i - 2]) % mod

    return dp[len(s)]


s = input()
dp = [0] * 5001
dp[0] = dp[1] = 1
mod = 1000000

print(solve(s))
# import sys

# input = sys.stdin.readline
# a = list(input().strip())
# len_a = len(a)
# dp = [0 for i in range(len_a + 1)]
# dp[0], dp[1] = 1, 1
# if a[0] == "0":
#     print(0)
# else:
#     for i in range(2, len_a + 1):
#         if int(a[i - 1]) > 0:
#             dp[i] += dp[i - 1]
#         num = int(a[i - 1]) + int(a[i - 2]) * 10
#         if num >= 10 and num <= 26:
#             dp[i] += dp[i - 2]
#     print(dp[len_a] % 1000000)