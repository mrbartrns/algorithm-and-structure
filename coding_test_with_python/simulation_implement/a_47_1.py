# BOJ 19236 (청소년 상어)
import sys
import copy

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


# initialize
def init():
    for i in range(4):
        for j in range(0, 8, 2):
            board[i][j // 2] = arr[i][j]
            fish = arr[i][j]
            table[fish] = [i, j // 2, arr[i][j + 1] - 1]

    fish = board[0][0]
    table[0] = [0, 0, table[fish][2]]
    table[fish] = [-1, -1, -1]
    board[0][0] = 0
    return fish


def move(board, table):
    for i in range(1, 17):
        if table[i][2] == -1:
            continue

        y, x, d = table[i]
        for _ in range(8):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                d = (d + 1) % 8

            elif board[ny][nx] == 0:
                d = (d + 1) % 8

            else:
                nxt = board[ny][nx]
                table[i] = [ny, nx, d]
                board[y][x], board[ny][nx] = nxt, i
                if nxt > 0:
                    table[nxt][0], table[nxt][1] = y, x
                break


def backtrack(board, table, ret, answer):
    move(board, table)
    for i in range(1, 5):
        b = copy.deepcopy(board)
        t = copy.deepcopy(table)
        y, x, d = t[0]
        ny = y + dy[d] * i
        nx = x + dx[d] * i

        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        if b[ny][nx] == -1:
            continue

        # 디버깅이 필요할 것 같은 부분 미리 표시하기
        b[y][x] = -1
        nxt = b[ny][nx]
        t[0] = [t[nxt][0], t[nxt][1], t[nxt][2]]
        t[nxt] = [-1, -1, -1]
        b[ny][nx] = 0
        ret.append(nxt)
        answer.append(copy.deepcopy(ret))
        backtrack(b, t, ret, answer)
        ret.pop()


table = [[-1, -1, -1] for _ in range(17)]
board = [[0 for _ in range(4)] for _ in range(4)]
arr = [list(map(int, si().split())) for _ in range(4)]
answer = 0
ret = []
f = init()
backtrack(board, table, [f], ret)
for i in range(len(ret)):
    answer = max(sum(ret[i]), answer)
print(answer)
