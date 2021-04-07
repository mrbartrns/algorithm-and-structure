# 멀리 뛰기
def solution(n):
    MOD = 1234567
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    return dp[n]