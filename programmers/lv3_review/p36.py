# 거스름돈
MOD = 1000000007


def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(len(money)):
        for j in range(1, n + 1):
            if j - money[i] >= 0:
                dp[j] = (dp[j] + dp[j - money[i]]) % MOD
    return dp[n]


if __name__ == "__main__":
    n = 5
    money = [1, 2, 5]
    print(solution(n, money))
