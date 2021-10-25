# BOJ 4883 삼각 그래프
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


tc = 0
while True:
    tc += 1
    N = int(si())
    if N == 0:
        break
    graph = [list(map(int, si().split(" "))) for _ in range(N)]
    dp = [[graph[i][j] for j in range(3)] for i in range(N)]
    dp[0][0] = INF
    dp[0][1] = graph[0][1]
    dp[0][2] = dp[0][1] + graph[0][2]
    for i in range(1, N):
        for j in range(3):
            s = INF
            if j - 1 >= 0:
                s = min(s, dp[i][j - 1])
            if i - 1 >= 0:
                s = min(s, dp[i - 1][j])
            if i - 1 >= 0 and j - 1 >= 0:
                s = min(s, dp[i - 1][j - 1])
            if i - 1 >= 0 and j + 1 < 3:
                s = min(s, dp[i - 1][j + 1])
            dp[i][j] = s + graph[i][j]
    print(f"{tc}. {dp[N - 1][1]}")
