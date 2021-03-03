# dp 피보나치
# dp는 이전의 입력사례를 그대로 사용할 수 있을 때 사용


def solution(n):
    dp = [0, 1]
    mod = 1234567
    for i in range(2, n + 1):
        dp.append((dp[i - 1] + dp[i - 2]) % mod)
    return dp[n]


print(solution(5))