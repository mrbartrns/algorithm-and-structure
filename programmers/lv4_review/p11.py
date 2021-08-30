# 3 * n 타일링
MOD = 1000000007


def solution(n):
    dp = [0] * 5001
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = (dp[i - 2] * 3) % MOD
        for j in range(4, i, 2):
            dp[i] += (dp[i - j] * 2) % MOD
        dp[i] = (dp[i] + 2) % MOD
    return dp[n]


if __name__ == '__main__':
    n = 4
    print(solution(n))
