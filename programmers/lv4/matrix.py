# 최적의 행렬
import sys

sys.setrecursionlimit(100000)
INF = 987654321


def solution(matrix_sizes):
    dp = [[INF for _ in range(len(matrix_sizes))] for _ in range(len(matrix_sizes))]
    solve(0, len(matrix_sizes) - 1, dp, matrix_sizes)
    return dp[0][len(matrix_sizes) - 1]


def solve(y, x, dp, matrix):
    if dp[y][x] < INF:
        return dp[y][x]

    if y == x:
        dp[y][x] = 0
        return dp[y][x]

    if y + 1 == x:
        dp[y][x] = matrix[y][0] * matrix[y][1] * matrix[x][1]
        return dp[y][x]

    for k in range(y, x):
        dp[y][x] = min(
            solve(y, k, dp, matrix) + solve(k + 1, x, dp, matrix) + matrix[y][0] * matrix[k][1] * matrix[x][1],
            dp[y][x])
    return dp[y][x]


if __name__ == '__main__':
    matrix_sizes = [[5, 3], [3, 10], [10, 6]]
    print(solution(matrix_sizes))
