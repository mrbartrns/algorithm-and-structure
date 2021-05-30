# BOJ 19237 (어른 상어)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def move_shark():
    graph = [[[] for _ in range(n)] for _ in range(n)]  # 무조건 순서대로 진입하게 됨
    for i in range(1, m + 1):
        if directions[i] == -1:
            continue

        y, x = locations[i]
        d = directions[i]
        chk = False

        for j in range(4):
            next_d = table[i - 1][d][j]

            ny = y + dy[next_d]
            nx = x + dx[next_d]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if smell[ny][nx][1] == 0:
                graph[ny][nx].append(i)
                locations[i] = [ny, nx]
                directions[i] = next_d
                chk = True
                break

        if not chk:
            for j in range(4):
                next_d = table[i - 1][d][j]

                ny = y + dy[next_d]
                nx = x + dx[next_d]

                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                if smell[ny][nx][0] == i:
                    graph[ny][nx].append(i)
                    locations[i] = [ny, nx]
                    directions[i] = next_d
                    break

    for y in range(n):
        for x in range(n):
            while len(graph[y][x]) > 1:
                cur_shark = graph[y][x].pop()
                locations[cur_shark] = [-1, -1]
                directions[cur_shark] = -1
                shark_cnt[0] -= 1


def add_smell():
    for y in range(n):
        for x in range(n):
            if smell[y][x][1] > 0:
                smell[y][x][1] -= 1

            if smell[y][x][1] == 0:
                smell[y][x][0] = 0

    for i in range(1, m + 1):
        if directions[i] == -1:
            continue

        y, x = locations[i]
        smell[y][x] = [i, k]


def init():
    for y in range(n):
        for x in range(n):
            if board[y][x] > 0:
                shark = board[y][x]
                locations[shark] = [y, x]
                smell[y][x] = [shark, k]


# input
n, m, k = map(int, si().split())
board = [list(map(int, si().split())) for _ in range(n)]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
shark_cnt = [m]
locations = [[0, 0] for _ in range(m + 1)]
directions = [-1] + list(map(lambda x: x - 1, list(map(int, si().split()))))
table = []
for _ in range(m):
    temp = []
    for _ in range(4):
        d1 = list(map(lambda x: x - 1, list(map(int, si().split()))))
        temp.append(d1)
    table.append(temp)

# init
init()

time = 0
flag = False
while time <= 1000:
    if shark_cnt[0] == 1:
        flag = True
        break
    move_shark()
    add_smell()
    time += 1

print(time if flag else -1)
