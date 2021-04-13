# BOJ 17143
import sys

si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def fish(idx):
    s = 0
    for i in range(R):
        if graph[i][idx] > -1:
            shark_idx = graph[i][idx]
            sharks[shark_idx][5] = False
            s += sharks[shark_idx][4]
            graph[i][idx] = -1
            break
    return s


def shark_move():
    size = len(sharks)
    for i in range(size):
        if not sharks[i][5]:
            continue
        y, x = sharks[i][0], sharks[i][1]
        speed = sharks[i][2]
        direction = sharks[i][3]
        for _ in range(speed):
            ny = y + dy[direction]
            nx = x + dx[direction]
            if nx < 0 or nx >= C or ny < 0 or ny >= R:
                if direction == 0:
                    direction = 1
                elif direction == 1:
                    direction = 0
                elif direction == 2:
                    direction = 3
                elif direction == 3:
                    direction = 2
                sharks[i][3] = direction
                ny = y + dy[direction]
                nx = x + dx[direction]
            sharks[i][0] = ny
            sharks[i][1] = nx
            y, x = ny, nx
        check(y, x, i)


def check(y, x, n_idx):
    if graph[y][x] == -1:
        graph[y][x] = n_idx
    else:
        idx = graph[y][x]
        if sharks[idx][4] > sharks[n_idx][4]:
            sharks[n_idx][5] = False
        else:
            sharks[idx][5] = False
            graph[y][x] = n_idx


R, C, m = map(int, si().split())
sharks = []
for _ in range(m):
    r, c, s, d, z = map(int, si().split())  # 행, 렬, 속력, 이동방향, 크기
    sharks.append([r - 1, c - 1, s, d - 1, z, True])
tot = 0
fish_man_idx = 0
graph = [[-1 for _ in range(C)] for _ in range(R)]
for i in range(len(sharks)):
    nr = sharks[i][0]
    nc = sharks[i][1]
    graph[nr][nc] = i

while fish_man_idx < C:
    tot += fish(fish_man_idx)
    graph = [[-1 for _ in range(C)] for _ in range(R)]
    shark_move()
    fish_man_idx += 1

print(tot)