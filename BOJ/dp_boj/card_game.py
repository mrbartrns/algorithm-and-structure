# BOJ 10835 카드 게임
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline


def solve(l, r):
    if l >= N or r >= N:
        return 0

    if dp[l][r] > -1:
        return dp[l][r]

    dp[l][r] = 0
    if right[r] < left[l]:
        dp[l][r] += right[r] + solve(l, r + 1)
    else:
        dp[l][r] = max(dp[l][r], solve(l + 1, r))
        dp[l][r] = max(dp[l][r], solve(l + 1, r + 1))
    return dp[l][r]


N = int(si())
left = list(map(int, si().split(" ")))
right = list(map(int, si().split(" ")))
dp = [[-1 for _ in range(N)] for _ in range(N)]
solve(0, 0)
print(dp[0][0])
