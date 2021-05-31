# BOJ 16235
import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def spring_and_summer():
    for y in range(n):
        for x in range(n):
            t = trees[y][x]
            size = len(t)
            for k in range(size):
                if t[k] <= land[y][x]:
                    land[y][x] -= t[k]
                    t[k] += 1
                else:
                    for _ in range(k, size):
                        land[y][x] += (t.pop()) // 2
                    break


def fall_and_winter():
    for y in range(n):
        for x in range(n):
            t = trees[y][x]
            size = len(t)
            for k in range(size):
                if t[k] % 5 == 0:
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        trees[ny][nx].appendleft(1)
            land[y][x] += fertilizer[y][x]


def check():
    cnt = 0
    for y in range(n):
        for x in range(n):
            cnt += len(trees[y][x])
    return cnt


n, m, k = map(int, si().split())

land = [[5 for _ in range(n)] for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
fertilizer = []
for _ in range(n):
    fertilizer.append(list(map(int, si().split())))
for _ in range(m):
    r, c, z = map(int, si().split())
    trees[r - 1][c - 1].append(z)

for _ in range(k):
    spring_and_summer()
    fall_and_winter()

print(check())
