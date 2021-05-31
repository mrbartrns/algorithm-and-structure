# BOJ 16235 (나무 재태크)
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

n, m, k = map(int, si().split())
fertilizer = [[5 for _ in range(n)] for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
additional = [list(map(int, si().split())) for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, si().split())
    trees[a - 1][b - 1].append(c)


def spring():
    for y in range(n):
        for x in range(n):
            tree = trees[y][x]
            cnt = len(tree)
            for i in range(len(tree)):
                if fertilizer[y][x] < tree[i]:
                    break
                fertilizer[y][x] -= tree[i]
                tree[i] += 1
                cnt -= 1

            for _ in range(cnt):
                t = tree.pop()
                fertilizer[y][x] += t // 2


def fall():
    for y in range(n):
        for x in range(n):
            tree = trees[y][x]
            for i in range(len(tree)):
                if tree[i] % 5 == 0:
                    for d in range(8):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if ny < 0 or ny >= n or nx < 0 or nx >= n:
                            continue
                        trees[ny][nx].appendleft(1)
            fertilizer[y][x] += additional[y][x]


for _ in range(k):
    spring()
    fall()
res = 0
for i in range(n):
    for j in range(n):
        res += len(trees[i][j])
print(res)
