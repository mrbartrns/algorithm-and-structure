# BOJ 19237 (어른 상어)
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def move():
    b = [[0 for _ in range(n)] for _ in range(n)]
    graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(1, m + 1):
        y, x, d = sharks[i]

        if d == -1:
            continue

        chk = False
        for j in range(4):
            nd = table[i - 1][d][j] - 1
            ny = y + dy[nd]
            nx = x + dx[nd]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if smell[ny][nx][1] > 0:
                continue

            chk = True
            sharks[i] = [ny, nx, nd]
            graph[ny][nx].append(i)
            break

        if not chk:
            for j in range(4):
                nd = table[i - 1][d][j] - 1
                ny = y + dy[nd]
                nx = x + dx[nd]

                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                if smell[ny][nx][0] == i:
                    sharks[i] = [ny, nx, nd]
                    graph[ny][nx].append(i)
                    break

    for y in range(n):
        for x in range(n):
            while len(graph[y][x]) > 1:
                dead = graph[y][x].pop()
                sharks[dead] = [-1, -1, -1]

    for y in range(n):
        for x in range(n):
            if graph[y][x]:
                b[y][x] = graph[y][x][0]

    return b


def add_smell():
    for i in range(1, m + 1):
        y, x, d = sharks[i]
        if d > -1:
            smell[y][x] = [i, k]


def remove_smell():
    for y in range(n):
        for x in range(n):
            if smell[y][x][1] > 0:
                smell[y][x][1] -= 1
                if smell[y][x][1] == 0:
                    smell[y][x][0] = 0


def check():
    for y in range(n):
        for x in range(n):
            if board[y][x] > 1:
                return False
    return True


n, m, k = map(int, si().split())
board = [list(map(int, si().split())) for _ in range(n)]
sharks = [[-1, -1, -1] for _ in range(m + 1)]
directions = list(map(int, si().split()))
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            shark = board[i][j]
            sharks[shark] = [i, j, directions[shark - 1] - 1]
table = []
for _ in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, si().split())))
    table.append(temp)


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