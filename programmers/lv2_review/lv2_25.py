# 가장 큰 정사각형 찾기
# 가장 큰, 경우의 수, 가장 작은 등등이 나올경우 다이나믹 프로그래밍으로 풀 수 있는지 확인
# 점차 하나씩 늘려가는것을 생각할 것


def solution(board):
    n, m = len(board), len(board[0])
    ans = 0
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = board[i - 1][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    for i in range(n + 1):
        for j in range(m + 1):
            ans = max(ans, dp[i][j])
    return ans * ans


board = [[0, 0, 1, 1], [1, 1, 1, 1]]
print(solution(board))