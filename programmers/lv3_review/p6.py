# 정수 삼각형
def solution(triangle):
    dp = [[0 for _ in range(500)] for _ in range(500)]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
            if j > 0:
                dp[i][j] = max(dp[i - 1][j - 1] + triangle[i][j], dp[i][j])
    return max(dp[len(triangle) - 1])


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))
