# 도둑질
def solution(money):
    dp = [0] * len(money)
    dp[0] = money[0]
    for i in range(1, len(money) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer = dp[len(money) - 2]
    dp = [0] * len(money)
    money.reverse()
    dp[0] = money[0]
    for i in range(1, len(money) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer = max(answer, dp[len(money) - 2])
    return answer


if __name__ == '__main__':
    money = [1, 2, 3, 1]
    print(solution(money))
