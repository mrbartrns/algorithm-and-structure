# BOJ 19237 (어른 상어)
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def add_smell():
    for i in range(1, m + 1):
        y, x, d = sharks[i]
        if d > -1:
            smell[y][x] = [i, k]


def move():
    graph = [[[] for _ in range(n)] for _ in range(n)]
    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, m + 1):
        y, x, d = sharks[i]

        if d == -1:
            continue

        chk = False
        # smell 있으면 -> 움직임
        for j in range(4):
            nd = table[i - 1][d][j] - 1
            ny = y + dy[nd]
            nx = x + dx[nd]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if smell[ny][nx][1] > 0:
                continue

            graph[ny][nx].append(i)
            sharks[i] = [ny, nx, nd]
            chk = True
            break

        if not chk:
            for j in range(4):
                nd = table[i - 1][d][j] - 1
                ny = y + dy[nd]
                nx = x + dx[nd]

                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                if smell[ny][nx][0] == i:
                    graph[ny][nx].append(i)
                    sharks[i] = [ny, nx, nd]
                    break

    for y in range(n):
        for x in range(n):
            while len(graph[y][x]) > 1:
                dead = graph[y][x].pop()
                sharks[dead] = [-1, -1, -1]

    for y in range(n):
        for x in range(n):
            if graph[y][x]:
                board[y][x] = graph[y][x][0]
    return board


def remove_smell():
    for y in range(n):
        for x in range(n):
            if smell[y][x][1] > 0:
                smell[y][x][1] -= 1
                if smell[y][x][1] == 0:
                    smell[y][x][0] = 0


def check():
    for i in range(n):
        for j in range(n):
            if board[i][j] > 1:
                return False
    return True


n, m, k = map(int, si().split())
sharks = [[-1, -1, -1] for _ in range(m + 1)]
board = [list(map(int, si().split())) for _ in range(n)]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
temp_d = list(map(int, si().split()))
table = [[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        table[i].append(list(map(int, si().split())))


for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            shark = board[i][j]
            sharks[shark] = [i, j, temp_d[shark - 1] - 1]  # inital y, x, d

cnt = 0
flag = False
while cnt <= 1000:
    if check():
        flag = True
        print(cnt)
        break
    add_smell()
    board = move()
    remove_smell()
    cnt += 1


if not flag:
    print(-1)