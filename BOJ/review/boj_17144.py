# BOJ 17144
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def air_conditioner():
    arr = []
    for i in range(n):
        if graph[i][0] == -1:
            arr.append((i, 0))
    return arr


def setting(air_conditioner_location):
    table = []
    temp = []
    sy, _ = air_conditioner_location[0]
    for i in range(sy - 1, -1, -1):
        temp.append((i, 0))
    for i in range(1, m):
        temp.append((0, i))
    for i in range(1, sy + 1):
        temp.append((i, m - 1))
    for i in range(m - 2, 0, -1):
        temp.append((sy, i))
    table.append(temp[:])
    temp.clear()
    sy, _ = air_conditioner_location[1]
    for i in range(sy + 1, n):
        temp.append((i, 0))
    for i in range(1, m):
        temp.append((n - 1, i))
    for i in range(n - 2, sy - 1, -1):
        temp.append((i, m - 1))
    for i in range(m - 2, 0, -1):
        temp.append((sy, i))
    table.append(temp[:])
    return table


def diffuse(dusts):
    for y in range(n):
        for x in range(m):
            if graph[y][x] > 0:
                cnt = 0
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny < 0 or ny >= n or nx < 0 or nx >= m:
                        continue
                    if graph[ny][nx] == -1:
                        continue
                    graph[ny][nx] += dusts[y][x]
                    graph[y][x] -= dusts[y][x]


def get_diffusion_value(maps):
    board = [[0 for _ in range(m)] for _ in range(n)]
    for y in range(n):
        for x in range(m):
            board[y][x] = maps[y][x] // 5
    return board


def operate(setting_table):
    counter_clockwise = deque()
    clockwise = deque()
    for i in range(len(setting_table[0])):
        y, x = setting_table[0][i]
        counter_clockwise.append(graph[y][x])
    for i in range(len(setting_table[1])):
        y, x = setting_table[1][i]
        clockwise.append(graph[y][x])

    counter_clockwise.popleft()
    counter_clockwise.append(0)
    clockwise.popleft()
    clockwise.append(0)

    for i in range(len(setting_table[0])):
        y, x = setting_table[0][i]
        graph[y][x] = counter_clockwise[i]

    for i in range(len(setting_table[1])):
        y, x = setting_table[1][i]
        graph[y][x] = clockwise[i]


def get_value():
    s = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] > 0:
                s += graph[y][x]
    return s


n, m, t = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
air_con_location = air_conditioner()
table = setting(air_con_location)
for _ in range(t):
    dusts = get_diffusion_value(graph)
    diffuse(dusts)
    operate(table)

print(get_value())
