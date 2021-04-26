# BOJ 19237
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 상어의 위치를 이동시키는 함수 (현재 상어의 위치 저장까지)
def move_shark():
    # 1부터 m까지의 상어 순회
    for shark in range(1, m + 1):
        available = False
        y, x, shark_direction = location[shark]
        for direction in direction_table[shark][shark_direction]:
            ny = y + dy[direction]
            nx = x + dx[direction]
            # 상어의 냄새가 아얘 없는 칸 먼저 찾기
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if smell[ny][nx][1] == 0:
                graph[y][x].pop()
                graph[ny][nx].append(shark)
                location[shark] = [ny, nx, direction]
                available = True
                break

        # 갈 수 있는 칸이 없다면 자기 자신의 냄새가 있는 곳으로 이동하기
        if not available:
            for direction in direction_table[shark][shark_direction]:
                ny = y + dy[direction]
                nx = x + dx[direction]
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                if smell[ny][nx][0] == shark:
                    graph[y][x].pop()
                    graph[ny][nx].append(shark)
                    location[shark] = [ny, nx, direction]
                    break


# 상어의 위치에 몇명 있는지 체크 후, 그 위치에 냄새 추가하기
def add_smell():
    for y in range(n):
        for x in range(n):
            # 기존의 냄새를 1씩 깎기
            if smell[y][x][1] > 0:
                smell[y][x][1] -= 1
                if smell[y][x][1] == 0:
                    smell[y][x][0] = 0
            while len(graph[y][x]) > 1:
                el = graph[y][x].pop()
                location[el] = [-1, -1, -1]
                left[0] -= 1

            # 냄새 추가하기
            if len(graph[y][x]) > 0:
                shark = graph[y][x][0]
                smell[y][x] = [shark, k]


n, m, k = map(int, si().split())
# 처음 graph
init_graph = [list(map(int, si().split())) for _ in range(n)]
graph = [[[] for _ in range(n)] for _ in range(n)]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
# 처음 direction
init_directions = [-1] + list(map(lambda x: x - 1, list(map(int, si().split()))))
direction_table = [[] for _ in range(m + 1)]
location = [[-1, -1, -1] for _ in range(m + 1)]  # y, x, d
left = [m]

# make direction_table
for i in range(1, m + 1):
    for _ in range(4):
        temp = list(map(lambda x: x - 1, list(map(int, si().split()))))
        direction_table[i].append(temp)

# 처음 상어 위치 저장
for i in range(n):
    for j in range(n):
        if init_graph[i][j] > 0:
            cur_shark = init_graph[i][j]
            graph[i][j].append(cur_shark)
            location[cur_shark] = [i, j, init_directions[cur_shark]]
            smell[i][j] = [cur_shark, k]

time = 0
flag = False
while time <= 1000:
    if left[0] == 1:
        flag = True
        break
    move_shark()
    add_smell()
    time += 1

print(time if flag else -1)

# for i in range(n):
#     print(graph[i])
# print()
#
# for i in range(n):
#     print(smell[i])
# print()
#
# for i in range(n):
#     print(location[i])
