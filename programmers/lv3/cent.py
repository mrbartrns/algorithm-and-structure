"""
거스름돈
dp[i][j]: i 인덱스의 돈 j원을 주었을 때 줄 수 있는 방법의 수
"""


def solution(n, money):
    """
    solution function to solve balance problem by using dynamic programming
    Args:
        n(int): balance
        money(list): coins

    Returns(int): case of paying balance

    """
    mod = 1000000007
    dp = [[0 for _ in range(n + 1)] for _ in range(len(money))]
    for i in range(len(money)):
        dp[i][0] = 1
    for j in range(1, n + 1):
        if j % money[0] == 0:
            dp[0][j] = 1

    for i in range(1, len(money)):
        for j in range(1, n + 1):
            if j - money[i] >= 0:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - money[i]]) % mod
            else:
                dp[i][j] = (dp[i - 1][j]) % mod
    answer = dp[len(money) - 1][n]
    return answer


if __name__ == "__main__":
    n = 10
    money = [1, 2, 5]
    print(solution(n, money))
