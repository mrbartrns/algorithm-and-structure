# BOJ 20057
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
sheet = [[(-1, 1, 1), (-1, 0, 7), (-2, 0, 2), (-1, -1, 10), (1, 1, 1), (1, 0, 7), (2, 0, 2), (1, -1, 10), (0, -2, 5)],
         [(-1, -1, 1), (0, -1, 7), (0, -2, 2), (1, -1, 10), (-1, 1, 1), (0, 1, 7), (0, 2, 2), (1, 1, 10), (2, 0, 5)],
         [(1, -1, 1), (1, 0, 7), (2, 0, 2), (1, 1, 10), (-1, -1, 1), (-1, 0, 7), (-2, 0, 2), (-1, 1, 10), (0, 2, 5)],
         [(1, 1, 1), (0, 1, 7), (0, 2, 2), (-1, 1, 10), (1, -1, 1), (0, -1, 7), (0, -2, 2), (-1, -1, 10), (-2, 0, 5)]]


def move(y, x, d, scale):
    t = 0
    while t < scale:
        ny = y + dy[d]
        nx = x + dx[d]
        y, x = ny, nx
        cnt[0] += spread(y, x, d)
        if y == 0 and x == 0:
            return y, x
        t += 1
    return y, x


def spread(y, x, d):
    over_scope = 0
    s = 0
    silicon = graph[y][x]
    for i in range(9):
        ty, tx, p = sheet[d][i]
        ny = y + ty
        nx = x + tx
        temp = silicon * p // 100
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            over_scope += temp
        else:
            graph[ny][nx] += temp
        s += temp
    if y + dy[d] < 0 or y + dy[d] >= n or x + dx[d] < 0 or x + dx[d] >= n:
        over_scope += silicon - s
    else:
        graph[y + dy[d]][x + dx[d]] += silicon - s

    graph[y][x] = 0

    return over_scope


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
st = (n // 2, n // 2)

r, c = st
d = 0
scale = 1
cnt = [0]
while True:
    r, c = move(r, c, d, scale)
    if r == 0 and c == 0:
        break
    d = (d + 1) % 4
    if d % 2 == 0:
        scale += 1

print(cnt[0])
