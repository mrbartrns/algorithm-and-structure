# BOJ 5069 미로에 갇힌 상근
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, -1, 1, 1, 1, -1]
dx = [0, -1, -1, 0, 1, 1]


def memoize(y, x, cnt):
    if dp[cnt][y][x] > -1:
        return dp[y][x]

    if cnt == n:
        if y == 50 and x == 50:
            dp[cnt][y][x] = 1
            return dp[cnt][y][x]
        dp[cnt][y][x] = 0
        return 0

    dp[cnt][y][x] = 0
    for i in range(6):
        ny = y + dy[i]
        nx = x + dx[i]
        dp[cnt][y][x] = 0


dp = [[[-1 for _ in range(100)] for _ in range(100)] for _ in range(15)]

t = int(si())
for _ in range(t):
    n = int(si())