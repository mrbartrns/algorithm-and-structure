# 멀리 뛰기
MOD = 1234567


def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    return dp[n]


if __name__ == "__main__":
    n = 4
    print(solution(n))
