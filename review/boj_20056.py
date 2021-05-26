# BOJ 20056 (마법사 상어와 파이어볼)
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

n, t, k = map(int, si().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(t):
    a1, a2, a3, a4, a5 = map(int, si().split())
    graph[a1 - 1][a2 - 1].append([a3, a4, a5])
dy = [n - 1, n - 1, 0, 1, 1, 1, 0, n - 1]
dx = [0, 1, 1, 1, 0, n - 1, n - 1, n - 1]


def move_ball(maps):
    ret = [[[] for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            while maps[y][x]:
                ball = maps[y][x].pop()
                m, s, d = ball

                ny = (y + dy[d] * s) % n
                nx = (x + dx[d] * s) % n

                ret[ny][nx].append([m, s, d])
    return ret


def combine(maps):
    for y in range(n):
        for x in range(n):
            if len(maps[y][x]) > 1:
                vector = maps[y][x]
                length = len(vector)
                sm, ss = 0, 0
                is_same = True
                first = vector[0][2] % 2  # direction -> odd even

                while vector:
                    m, s, d = vector.pop()
                    sm += m
                    ss += s
                    if is_same and first != d % 2:
                        is_same = False

                ave_m = sm // 5
                ave_s = ss // length
                if ave_m > 0:
                    for i in range(0, 8, 2):
                        if is_same:
                            vector.append([ave_m, ave_s, i])
                        else:
                            vector.append([ave_m, ave_s, i + 1])


for _ in range(k):
    graph = move_ball(graph)
    combine(graph)

res = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            for p in range(len(graph[i][j])):
                res += graph[i][j][p][0]
print(res)
