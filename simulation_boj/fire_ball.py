# BOJ 20056
import sys

# sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

n, m, k = map(int, si().split())
dy = [n - 1, n - 1, 0, 1, 1, 1, 0, n - 1]
dx = [0, 1, 1, 1, 0, n - 1, n - 1, n - 1]

balls = []
for _ in range(m):
    r, c, m, s, d = map(int, si().split())
    balls.append([r - 1, c - 1, m, s, d])


def move(fireballs):
    graph = [[[] for _ in range(n)] for _ in range(n)]
    for y, x, m, s, d in fireballs:
        ny = (y + dy[d] * s) % n
        nx = (x + dx[d] * s) % n
        graph[ny][nx].append([m, s, d])
    return graph


def sum_fireballs(graph):
    new_balls = []
    for y in range(n):
        for x in range(n):
            if len(graph[y][x]) >= 2:
                cur_fireballs = graph[y][x][:]
                size = len(cur_fireballs)
                sm = 0
                ss = 0
                same = True
                for i in range(size):
                    m, s, d = cur_fireballs[i]
                    sm += m
                    ss += s
                    if d % 2 != cur_fireballs[0][2] % 2:
                        same = False
                ave_sm = sm // 5
                ave_ss = ss // size
                if ave_sm > 0:
                    for i in range(4):
                        if same:
                            new_balls.append([y, x, ave_sm, ave_ss, i * 2])
                        else:
                            new_balls.append([y, x, ave_sm, ave_ss, i * 2 + 1])
            else:
                if graph[y][x]:
                    m, s, d = graph[y][x][0]
                    new_balls.append([y, x, m, s, d])

    return new_balls


for _ in range(k):
    maps = move(balls)
    balls = sum_fireballs(maps)

res = 0
for i in range(len(balls)):
    res += balls[i][2]
print(res)
