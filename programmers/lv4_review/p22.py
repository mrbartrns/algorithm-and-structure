INF = 987654321


def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[INF for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for i in range(n - 1):
        dp[i][i + 1] = matrix_sizes[i][0] * matrix_sizes[i][1] * matrix_sizes[i + 1][1]

    for cnt in range(1, n):
        for i in range(n - cnt):
            j = i + cnt
            for k in range(i, j):
                dp[i][j] = min(dp[i][j],
                               (dp[i][k] + dp[k + 1][j]) + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1])

    return dp[0][len(matrix_sizes) - 1]


if __name__ == '__main__':
    matrix_size = [[5, 3], [3, 10], [10, 6]]
    print(solution(matrix_size))
