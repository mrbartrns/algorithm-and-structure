# 정수 삼각형
def solution(triangle):
    dp = [[-1 for _ in range(len(triangle))] for _ in range(len(triangle))]
    for i in range(len(triangle)):
        dp[0][i] = 0
    dp[0][0] = triangle[0][0]
    for i in range(len(triangle)):
        solve(len(triangle) - 1, i, dp, triangle)
    return max(dp[len(triangle) - 1])


def solve(y, x, dp, triangle):
    if y == 0:
        return dp[y][x]

    if x >= len(triangle[y]):
        return 0

    if dp[y][x] > -1:
        return dp[y][x]

    dp[y][x] = solve(y - 1, x, dp, triangle) + triangle[y][x]
    if x > 0:
        dp[y][x] = max(dp[y][x], solve(y - 1, x - 1, dp, triangle) + triangle[y][x])
    return dp[y][x]


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))
