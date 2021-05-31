# BOJ 20057 (마법사 상어와 토네이도)
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def move(y, x, scale, d):
    i = 0
    while i < scale:
        ny = y + dy[d]
        nx = x + dx[d]
        y, x = ny, nx
        if graph[y][x] > 0:
            cnt[0] += spread(y, x, d)
        if y == 0 and x == 0:
            return y, x
        i += 1
    return y, x


def spread(y, x, d):
    amount = graph[y][x]
    s = 0
    tot = 0
    for i in range(len(table[d])):
        ndy, ndx, p = table[d][i]
        ny = y + ndy
        nx = x + ndx
        val = amount * p // 100
        tot += val
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            s += val
            continue
        graph[ny][nx] += val
    if y + dy[d] < 0 or y + dy[d] >= n or x + dx[d] < 0 or x + dx[d] >= n:
        s += amount - tot
    else:
        graph[y + dy[d]][x + dx[d]] += amount - tot
    graph[y][x] = 0
    return s


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
table = [
    [
        (-1, 1, 1),
        (-1, 0, 7),
        (-2, 0, 2),
        (-1, -1, 10),
        (1, 1, 1),
        (1, 0, 7),
        (2, 0, 2),
        (1, -1, 10),
        (0, -2, 5),
    ],
    [
        (-1, -1, 1),
        (0, -1, 7),
        (0, -2, 2),
        (1, -1, 10),
        (-1, 1, 1),
        (0, 1, 7),
        (0, 2, 2),
        (1, 1, 10),
        (2, 0, 5),
    ],
    [
        (1, -1, 1),
        (1, 0, 7),
        (2, 0, 2),
        (1, 1, 10),
        (-1, -1, 1),
        (-1, 0, 7),
        (-2, 0, 2),
        (-1, 1, 10),
        (0, 2, 5),
    ],
    [
        (1, 1, 1),
        (0, 1, 7),
        (0, 2, 2),
        (-1, 1, 10),
        (1, -1, 1),
        (0, -1, 7),
        (0, -2, 2),
        (-1, -1, 10),
        (-2, 0, 5),
    ],
]

t = 1
direction = 0
r, c = n // 2, n // 2
cnt = [0]
while True:
    r, c = move(r, c, t, direction)
    if r == 0 and c == 0:
        break
    direction = (direction + 1) % 4
    if direction % 2 == 0:
        t += 1
print(cnt[0])
