# BOJ 19237 (어른상어)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def shark_move():
    for shark in range(1, m + 1):
        available = False
        y, x = locations[shark]
        d = directions[shark]

        if y == -1 and x == -1 and d == -1:
            continue

        for next_d in table[shark][d]:
            ny = y + dy[next_d]
            nx = x + dx[next_d]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if smell[ny][nx][1] > 0:
                continue

            if smell[ny][nx][1] == 0:
                board[y][x].pop()
                board[ny][nx].append(shark)
                locations[shark] = [ny, nx]
                directions[shark] = next_d
                available = True
                break

        if not available:
            for next_d in table[shark][d]:
                ny = y + dy[next_d]
                nx = x + dx[next_d]

                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                if smell[ny][nx][0] == shark:
                    board[y][x].pop()
                    board[ny][nx].append(shark)
                    locations[shark] = [ny, nx]
                    directions[shark] = next_d
                    break


def add_smell():
    for y in range(n):
        for x in range(n):
            if smell[y][x][1] > 0:
                smell[y][x][1] -= 1
                if smell[y][x][1] == 0:
                    smell[y][x][0] = 0

            while len(board[y][x]) > 1:
                el = board[y][x].pop()
                locations[el] = [-1, -1]
                directions[el] = -1
                left[0] -= 1

            # 냄새 추가
            if board[y][x] > 0:
                shark = board[y][x][0]
                smell[y][x] = [shark, k]


# initialize
n, m, k = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
board = [[[] for _ in range(n)] for _ in range(n)]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
table = [[] for _ in range(m + 1)]  # table[shark_number - 1][current_direction][priority]

directions = [-1] + list(map(int, si().split()))  # direction is 1, 2, 3, 4
locations = [[0, 0] for _ in range(m + 1)]
left = [m]
for i in range(1, m + 1):
    for _ in range(4):
        a1, a2, a3, a4 = map(int, si().split())
        table[i].append([a1 - 1, a2 - 1, a3 - 1, a4 - 1])

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        this_shark = graph[i][j]
        board[i][j].append(this_shark)
        smell[i][j][0] = this_shark
        smell[i][j][1] = k
        locations[this_shark - 1] = [i, j]

# use board and smell, table after this line
time = 0
chk = False
while time <= 1000:
    if left[0] == 1:
        chk = True
        break
    shark_move()
    add_smell()
    time += 1
print(time if chk else -1)
