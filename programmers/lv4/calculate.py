# 사칙연산
INF = 987654321


def solution(arr):
    n = (len(arr) // 2) + 1
    max_dp = [[-INF for _ in range(n)] for _ in range(n)]
    min_dp = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        max_dp[i][i] = int(arr[i * 2])
        min_dp[i][i] = int(arr[i * 2])

    for cnt in range(1, n):
        for i in range(n - cnt):
            j = i + cnt
            for k in range(i, j):
                if arr[k * 2 + 1] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])
    return max_dp[0][n - 1]


if __name__ == '__main__':
    arr = ["1", "-", "3", "+", "5", "-", "8"]
    print(solution(arr))
