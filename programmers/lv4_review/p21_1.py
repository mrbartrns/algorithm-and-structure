# 최적의 행렬 곱셈
INF = 987654321


def solution(matrix_sizes):
    dp = [[INF for _ in range(len(matrix_sizes))] for _ in range(len(matrix_sizes))]
    for i in range(len(dp)):
        dp[i][i] = 0
        if i + 1 < len(dp):
            dp[i][i + 1] = (
                matrix_sizes[i][0] * matrix_sizes[i][1] * matrix_sizes[i + 1][1]
            )

    for cnt in range(1, len(dp)):
        for i in range(len(dp) - cnt):
            j = i + cnt
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j],
                    (dp[i][k] + dp[k + 1][j])
                    + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1],
                )
    return dp[0][len(dp) - 1]


if __name__ == "__main__":
    matrix_sizes = [[5, 3], [3, 10], [10, 6]]
    print(solution(matrix_sizes))