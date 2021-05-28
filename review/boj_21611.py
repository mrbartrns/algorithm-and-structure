# BOJ 21611 (마법사 상어와 블리자드)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def setting(size):
    ret = []
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    y, x = size // 2, size // 2
    d = 0
    t = 1
    while True:
        if y == 0 and x == 0:
            break
        i = 0
        while i < t:
            ny = y + dy[d]
            nx = x + dx[d]
            y, x = ny, nx
            ret.append((y, x))
            if y == 0 and x == 0:
                break
            i += 1
        d = (d + 1) % 4
        if d % 2 == 0:
            t += 1
    return ret


def get_arr():
    ret = []
    for y, x in locations:
        if graph[y][x] > 0:
            ret.append(graph[y][x])
    return ret


def pull(values):
    for i in range(len(locations)):
        y, x = locations[i]
        if i >= len(values):
            graph[y][x] = 0
        else:
            graph[y][x] = values[i]


def bomb():
    values = get_arr()
    while True:
        flag = False
        cnt = 0
        val = values[0]
        stack = []
        for i in range(len(values)):
            if not stack or val == values[i]:
                cnt += 1
            else:
                if cnt >= 4:
                    while stack and val == stack[-1]:
                        stack.pop()
                    marble_score[val] += cnt
                    flag = True
                cnt = 1
            val = values[i]
            stack.append(values[i])
        values = stack[:]
        if not flag:
            return values


def spell(d, s):
    i = 0
    y, x = n // 2, n // 2
    while i < s:
        ny = y + dy[d]
        nx = x + dx[d]
        graph[ny][nx] = 0
        y, x = ny, nx
        i += 1


def revolute():
    values = get_arr()
    ret = []
    if values:
        val = values[0]
        cnt = 0
        for i in range(len(values)):
            if val == values[i]:
                cnt += 1
            else:
                ret.append(cnt)
                ret.append(val)
                cnt = 1
            val = values[i]
        ret.append(cnt)
        ret.append(val)
    return ret


def print_graph():
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=" ")
        print()
    print()


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
locations = setting(n)
marble_score = [0, 0, 0, 0]
orders = []
for _ in range(m):
    a1, a2 = map(int, si().split())
    orders.append((a1 - 1, a2))

for direction, speed in orders:
    spell(direction, speed)
    marble_values = get_arr()
    pull(marble_values)
    marble_values = bomb()
    pull(marble_values)
    marble_values = revolute()
    pull(marble_values)

score = marble_score[1] * 1 + marble_score[2] * 2 + marble_score[3] * 3
print(score)
