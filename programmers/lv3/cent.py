"""
거스름돈
dp[i][j]: i 인덱스의 돈 j원을 주었을 때 줄 수 있는 방법의 수
"""


def solution(n, money):
    answer = 0
    dp = [[0 for _ in range(n + 1)] for _ in range(len(money) + 1)]
    return answer
