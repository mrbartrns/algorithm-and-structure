# 개미 전사
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def solve(n):
    """
    리스트의 n번째 인덱스를 선택했을 때 얻을 수 있는 최댓값을 반환한다.

    Args:
        n: index of array

    Returns(int): returns maximum value of problem

    """
    if n == 0:
        dp[n] = arr[n]
        return dp[n]

    if n == 1:
        dp[n] = max(arr[n - 1], arr[n])
        return dp[n]

    if dp[n] > 0:
        return dp[n]

    dp[n] = max(solve(n - 1), solve(n - 2) + arr[n])
    return dp[n]


arr = list(map(int, si().split()))
dp = [0] * 100
n = len(arr)
# print(solve(n - 1))
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])
print(dp[n - 1])
