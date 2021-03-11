def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    unable = [[False for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(len(puddles)):
        y = puddles[i][0]
        x = puddles[i][1]
        unable[x][y] = True

    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if unable[i][j]:
                continue
            if i == j == 1:
                continue
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
    return dp[n][m]


m = 100
n = 100
puddles = [[1, 2]]
print(solution(m, n, puddles))
