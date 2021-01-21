# BOJ 9465

n = 5
stickers = [[50, 10, 100, 20, 40], [30, 50, 70, 10, 60]]
memo = [[0 for _ in range(n)] for _ in range(2)]
memo[0][0] = stickers[0][0]
memo[0][1] = stickers[0][1]


def solve(n):
    for i in range(1, n):
        if i < 2:
            memo[0][i] = memo[1][i - 1] + stickers[0][i]
            memo[1][i] = memo[0][i - 1] + stickers[1][i]
        else:
            memo[0][i] = max(memo[1][i - 1], memo[0][i - 2]) + stickers[0][i]
            memo[1][i] = max(memo[0][i - 1], memo[1][i - 2]) + stickers[1][i]
    return max(memo[0][n - 1], memo[1][n - 1])