# BOJ 3108
import sys

si = sys.stdin.readline
sys.setrecursionlimit(10000000)
# 어떻게 접근해야될지 모르겠다면 하나하나 해결하기
# 문제에서 주어진 그대로 사각형을 만들어보기

board = [[0 for _ in range(2001)] for _ in range(2001)]  # 좌표 * 2배씩 해서 문제 해결하기

t = int(si())
for _ in range(t):
    # 음수 좌표의 경우 그 수만큼 더해서 모두 양수로 만든다.
    x1, y1, x2, y2 = map(int, si().split())
    x1 = (x1 + 500) * 2
    y1 = (y1 + 500) * 2
    x2 = (x2 + 500) * 2
    y2 = (y2 + 500) * 2

    for i in range(x1, x2 + 1):
        board[i][y1] = board[i][y2] = 1
    for j in range(y1, y2 + 1):
        board[x1][j] = board[x2][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        return False

    # 같은 선을 여러번 지나갈 수 있기때문에 0으로 두면 안된다
    if board[x][y] == 1:
        board[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


cnt = 0
if board[1000][1000] == 1:
    cnt -= 1
for i in range(len(board)):
    for j in range(len(board[0])):
        if dfs(i, j):
            cnt += 1

# 마지막에 있는지 없는지 검사해야하므로

sys.stdout.write(str(cnt))