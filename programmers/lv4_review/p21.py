# 올바른 괄호의 갯수

def solution(n):
    dp = [0] * 15
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
    return dp[n]


if __name__ == '__main__':
    n = 3
    print(solution(n))
