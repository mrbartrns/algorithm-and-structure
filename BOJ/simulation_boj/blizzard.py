# BOJ 21611
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def setting(n):
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    max_cnt = 1
    y, x = n // 2, n // 2
    d = 0
    ret = []
    while True:
        cnt = 0
        while cnt < max_cnt:
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or nx < 0:
                break
            ret.append((ny, nx))
            cnt += 1
            y, x = ny, nx
        if y == 0 and x == 0:
            break
        d = (d + 1) % 4
        if d % 2 == 0:
            max_cnt += 1
    return ret


def get_value(location):
    que = deque(location)
    ret = []
    while que:
        y, x = que.popleft()
        if graph[y][x] > 0:
            ret.append(graph[y][x])
    return ret


def connect(location, values):
    for i in range(len(location)):
        r, c = location[i]
        if i < len(values):
            graph[r][c] = values[i]
        else:
            graph[r][c] = 0


def spell(d, s, n):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    y, x = n // 2, n // 2
    for i in range(1, s + 1):
        ny = y + dy[d] * i
        nx = x + dx[d] * i
        graph[ny][nx] = 0


def bomb(location):
    ret = []
    temp = []
    for i in range(len(location)):
        y, x = location[i]
        if graph[y][x] == 0:
            break
        if temp and graph[temp[-1][0]][temp[-1][1]] != graph[y][x]:
            if len(temp) >= 4:
                ret.append(temp[:])
            temp.clear()
        temp.append((y, x))
    if len(temp) >= 4:
        ret.append(temp)
    if ret:
        for i in range(len(ret)):
            for j in range(len(ret[i])):
                y, x = ret[i][j]
                marbles[graph[y][x]] += 1
                graph[y][x] = 0
        return True
    return False


def change(location):
    ret = []
    group = []
    for i in range(len(location)):
        y, x = location[i]
        if graph[y][x] == 0:
            break
        if group and graph[group[-1][0]][group[-1][1]] != graph[y][x]:
            ret.append((group[:]))
            group.clear()
        group.append((y, x))
    if group:
        ret.append(group)
    res = []
    for i in range(len(ret)):
        length = len(ret[i])
        number = graph[ret[i][0][0]][ret[i][0][1]]
        res.append(length)
        res.append(number)
    return res


def print_graph():
    for i in range(N):
        print(graph[i])
    print()


N, M = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(N)]
order = []
marbles = [0, 0, 0, 0]
score = 0
loc = setting(N)
for _ in range(M):
    d, s = map(int, si().split())
    order.append((d - 1, s))

for d, s in order:
    spell(d, s, N)
    val = get_value(loc)
    connect(loc, val)
    while bomb(loc):
        val = get_value(loc)
        connect(loc, val)
    # 구슬
    # print_graph()
    val = change(loc)
    connect(loc, val)
    # print_graph()

for i in range(4):
    score += i * marbles[i]

print(score)
