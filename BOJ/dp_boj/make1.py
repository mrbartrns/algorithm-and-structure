# BOJ 12852
import sys

si = sys.stdin.readline
MAX = int(1e9)


# 상향식으로 변경하기
# def solve(n):
#     if n == 1:
#         dp[n] = 0
#         return dp[n]
#     if dp[n] < MAX:
#         return dp[n]
#     dp[n] = min(dp[n], solve(n - 1) + 1)
#     if n % 3 == 0:
#         dp[n] = min(dp[n], solve(n // 3) + 1)
#     if n % 2 == 0:
#         dp[n] = min(dp[n], solve(n // 2) + 1)
#     return dp[n]

def solve(n):
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i])
        if i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i])
    return dp[n]


n = int(si())
dp = [MAX] * (n + 1)
res = []
ret = solve(n)
res.append(n)
t = n
while t > 1:
    temp = dp[t]
    val = t
    if temp > dp[t - 1]:
        val = t - 1
        temp = dp[t - 1]
    if t % 2 == 0 and temp > dp[t // 2]:
        val = t // 2
        temp = dp[t // 2]
    if t % 3 == 0 and temp > dp[t // 3]:
        val = t // 3
        temp = dp[t // 3]
    res.append(val)
    t = val
print(ret)
print(" ".join(list(map(str, res))))
