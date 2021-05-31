# BOJ 12100 2048(EASY)
import copy
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def move(d, maps):
    if d == 0:
        for x in range(n):
            for y in range(n - 1, -1, -1):
                if maps[y][x] == 0:
                    for k in range(y, n - 1):
                        maps[k][x], maps[k + 1][x] = maps[k + 1][x], maps[k][x]

    elif d == 1:
        for x in range(n):
            for y in range(n):
                if maps[y][x] == 0:
                    for k in range(y, 0, -1):
                        maps[k][x], maps[k - 1][x] = maps[k - 1][x], maps[k][x]

    elif d == 2:
        for y in range(n):
            for x in range(n - 1, -1, -1):
                if maps[y][x] == 0:
                    for k in range(x, n - 1):
                        maps[y][k], maps[y][k + 1] = maps[y][k + 1], maps[y][k]

    else:
        for y in range(n):
            for x in range(n):
                if maps[y][x] == 0:
                    for k in range(x, 0, -1):
                        maps[y][k], maps[y][k - 1] = maps[y][k - 1], maps[y][k]


def integrate(d, maps):
    if d == 0:
        for x in range(n):
            for y in range(n - 1):
                if maps[y][x] == maps[y + 1][x]:
                    maps[y][x] += maps[y + 1][x]
                    maps[y + 1][x] = 0
    elif d == 1:
        for x in range(n):
            for y in range(n - 1, 0, -1):
                if maps[y][x] == maps[y - 1][x]:
                    maps[y][x] += maps[y - 1][x]
                    maps[y - 1][x] = 0
    elif d == 2:
        for y in range(n):
            for x in range(n - 1):
                if maps[y][x] == maps[y][x + 1]:
                    maps[y][x] += maps[y][x + 1]
                    maps[y][x + 1] = 0
    else:
        for y in range(n):
            for x in range(n - 1, 0, -1):
                if maps[y][x] == maps[y][x - 1]:
                    maps[y][x] += maps[y][x - 1]
                    maps[y][x - 1] = 0


def get_max_value(maps):
    ret = 0
    for y in range(n):
        for x in range(n):
            ret = max(ret, maps[y][x])
    return ret


def backtrack(idx, k):
    if idx == k:
        copied_maps = copy.deepcopy(graph)
        for d in angle:
            move(d, copied_maps)
            integrate(d, copied_maps)
            move(d, copied_maps)
        ret = get_max_value(copied_maps)
        res[0] = max(res[0], ret)
        return

    for i in range(4):
        angle.append(i)
        backtrack(idx + 1, k)
        angle.pop()


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
angle = []
res = [0]

# for t in range(1, 6):
#     backtrack(0, t)
# 백트래킹을 5번 하는것이 4번하는것보다 항상 크거나 같다.

print(res[0])
