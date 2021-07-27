import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def shark_move(sharks, smell):
    graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(1, m + 1):
        y, x, d = sharks[i]

        if d == -1:
            continue

        chk = False

        for j in range(4):
            nd = table[i - 1][d][j]
            ny = y + dy[nd]
            nx = x + dx[nd]
            # smell check
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if smell[ny][nx][1] > 0:
                continue

            sharks[i] = [ny, nx, nd]
            graph[ny][nx].append(i)
            chk = True
            break

        if not chk:
            for j in range(4):
                nd = table[i - 1][d][j]
                ny = y + dy[nd]
                nx = x + dx[nd]

                # smell check
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                if smell[ny][nx][0] == i:
                    sharks[i] = [ny, nx, nd]
                    graph[ny][nx].append(i)
                    break

    for y in range(n):
        for x in range(n):
            while len(graph[y][x]) > 1:
                cur_shark = graph[y][x].pop()
                sharks[cur_shark] = [-1, -1, -1]

    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                board[i][j] = graph[i][j][0]
    return board


def add_smell(smell):
    for i in range(1, m + 1):
        y, x, d = sharks[i]
        if d > -1:
            smell[y][x] = [i, k]


def remove_smell(smell):
    for y in range(n):
        for x in range(n):
            if smell[y][x][1] > 0:
                smell[y][x][1] -= 1
                if smell[y][x][1] == 0:
                    smell[y][x][0] = 0


def check(board):
    for y in range(n):
        for x in range(n):
            if board[y][x] >= 2:
                return False
    return True


n, m, k = map(int, si().split())
board = [list(map(int, si().split())) for _ in range(n)]
sharks = [[0, 0, 0] for _ in range(m + 1)]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
ds = list(map(int, si().split()))
table = []

# make direction table
for _ in range(m):
    t = []
    for _ in range(4):
        arr = list(map(lambda x: x - 1, list(map(int, si().split()))))
        t.append(arr)
    table.append(t)

# initialize
for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            sharks[board[i][j]] = [i, j, ds[board[i][j] - 1] - 1]
            smell[i][j] = [board[i][j], k]


cnt = 0
flag = False
while cnt <= 1000:
    if check(board):
        flag = True
        print(cnt)
        break
    board = shark_move(sharks, smell)
    remove_smell(smell)
    add_smell(smell)

    cnt += 1
if not flag:
    print(-1)