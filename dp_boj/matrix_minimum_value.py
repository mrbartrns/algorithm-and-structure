# 행렬에서 최소 이동 비용 구하기
INF = 987654321
matrix = [[1, 3, 5, 8],
          [4, 2, 1, 7],
          [4, 3, 2, 3]]

dp = [[INF for _ in range(4)] for _ in range(3)]

ir = 2
ic = 3


def solve(r, c):
    if r == c == 0:
        return matrix[r][c]

    s = INF
    if r - 1 >= 0:
        s = min(s, solve(r - 1, c))
    if c - 1 >= 0:
        s = min(s, solve(r, c - 1))
    s += matrix[r][c]

    return s


def solve_cache(r, c):
    if r == c == 0:
        dp[r][c] = matrix[r][c]
        return dp[r][c]

    if dp[r][c] < INF:
        return dp[r][c]

    if r - 1 >= 0:
        dp[r][c] = min(dp[r][c], solve(r - 1, c))
    if c - 1 >= 0:
        dp[r][c] = min(dp[r][c], solve(r, c - 1))
    dp[r][c] += matrix[r][c]
    return dp[r][c]


def dynamic(r, c):
    dp[0][0] = 0
    for i in range(r + 1):
        for j in range(c + 1):
            if i - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
            if j - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1])
            dp[i][j] += matrix[i][j]
    return dp[r][c]


print(dynamic(2, 3))
