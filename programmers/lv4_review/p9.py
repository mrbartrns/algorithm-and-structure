def solution(money):
    n = len(money) - 1
    dp = [0] * n
    dp[0] = money[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])
    answer = dp[n - 1]
    money.reverse()
    dp = [0] * n
    dp[0] = money[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer = max(answer, dp[n - 1])
    return answer


if __name__ == '__main__':
    money = [1, 2, 3, 1]
    print(solution(money))
