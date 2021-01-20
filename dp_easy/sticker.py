# BOJ 9465
import sys

input = sys.stdin.readline


def solve(n):
    for i in range(1, n):
        memo[0][i] = max(memo[1][i - 1], memo[1][i - 2]) + stickers[0][i]
        memo[1][i] = max(memo[0][i - 1], memo[0][i - 2]) + stickers[1][i]
    return max(memo[0][n - 1], memo[1][n - 1])


t = int(input())
for _ in range(t):
    n = int(input())
    stickers = []
    memo = [[0 for _ in range(n)] for _ in range(2)]
    for _ in range(2):
        sticker = list(map(int, input().split()))
        stickers.append(sticker)
    memo[0][0], memo[1][0] = stickers[0][0], stickers[1][0]

    print(solve(n))