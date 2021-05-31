# BOJ 2186
import sys

si = sys.stdin.readline
# BFS로 접근시 너무 많은 메모리를 사용하여 메모리 초과가 남

"""
dfs를 사용시 어디서 메모이제이션을 하는것인지?
기본적으로 2차원 배열로 메모이제이션이 안될 때, 더 다차원의 dp 배열을 고려하는 연습 하기
dp[x][y][z] = x, y에 존재하는 알파벳을 찾고자하는 문자열의 c번 인덱스로 설정했을 때, 나올수 있는 정답의 갯수
"""


def dfs(x, y, k, c, word):
    if c == word:
        return 1

    if len(c) >= len(word):
        return 0

    cnt = 0
    for j in range(1, k + 1):
        for i in range(4):
            nx = x + (j * dx[i])
            ny = y + (j * dy[i])
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # dp[nx][ny] = dp[x][y] + board[nx][ny]
            # print(dp[nx][ny])
            cnt += dfs(nx, ny, k, c + board[nx][ny], word)
    return cnt


"""
n, m, k = map(int, si().split())
board = []
for _ in range(n):
    board.append(list(si().strip()))

word = si().strip()
"""

n = 4
m = 4
k = 1
board = [
    ["K", "A", "K", "T"],
    ["X", "E", "A", "S"],
    ["Y", "R", "W", "U"],
    ["Z", "B", "Q", "P"],
]
dp = [["" for _ in range(m)] for _ in range(n)]
word = "BREAK"


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == word[0]:
            # dp[y][x] = board[y][x]
            res += dfs(i, j, k, board[i][j], word)

sys.stdout.write(str(res))