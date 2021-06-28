# 2 * n 타일링
def solution(n):
    mod = 1000000007
    dp = [0] * 600001
    dp[0], dp[1] = 1, 1
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    return dp[n]


if __name__ == "__main__":
    n = 4
    print(solution(n))
