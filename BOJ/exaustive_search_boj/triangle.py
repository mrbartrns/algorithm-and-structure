# 정수 삼각형
def solution(triangle):
    size = len(triangle[-1])
    MAX = 0
    dp = [[0 for _ in range(size)] for _ in range(size)]
    dp[0][0] = triangle[0][0]
    for i in range(1, size):
        for j in range(len(triangle[i])):
            val = dp[i - 1][j] + triangle[i][j]
            if j > 0:
                val = max(val, dp[i - 1][j - 1] + triangle[i][j])
            dp[i][j] = val
            if MAX < val:
                MAX = val

    return MAX


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))