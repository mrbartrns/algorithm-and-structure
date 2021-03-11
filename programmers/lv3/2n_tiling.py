# 2 * n 타일링
def solution(n):
    dp = [0] * 60001
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    return dp[n]


print(solution(4))