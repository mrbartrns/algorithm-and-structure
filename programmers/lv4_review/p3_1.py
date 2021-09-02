INF = 987654321


def solution(arr):
    size = len(arr) // 2 + 1
    min_dp = [[INF for _ in range(size)] for _ in range(size)]
    max_dp = [[-INF for _ in range(size)] for _ in range(size)]
    for i in range(size):
        min_dp[i][i] = int(arr[2 * i])
        max_dp[i][i] = int(arr[2 * i])
    for cnt in range(1, size):
        for i in range(size - cnt):
            j = i + cnt
            for k in range(i, j):
                if arr[2 * k + 1] == "+":
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])
    return max_dp[0][size - 1]


if __name__ == '__main__':
    arr = ["1", "-", "3", "+", "5", "-", "8"]
    print(solution(arr))
