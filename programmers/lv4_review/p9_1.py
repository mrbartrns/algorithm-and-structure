# [도둑질]
def solution(money):
    dp = [0] * (len(money) - 1)
    dp[0] = money[0]
    for i in range(1, len(dp)):
        dp[i] = max(money[i] + dp[i - 2], dp[i - 1])
    answer = dp[-1]
    money.reverse()
    dp = [0] * (len(money) - 1)
    dp[0] = money[0]
    for i in range(1, len(dp)):
        dp[i] = max(money[i] + dp[i - 2], dp[i - 1])
    answer = max(answer, dp[-1])
    return answer


if __name__ == '__main__':
    money = [1, 2, 3, 1]
    print(solution(money))
