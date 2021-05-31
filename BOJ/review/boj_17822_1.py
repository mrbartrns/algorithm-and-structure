# BOJ 17822
import sys
from collections import deque
from functools import reduce

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def rotate(p, k):
    for i in range(p, n + 1, p):
        graph[i - 1].rotate(k)


def bfs(y, x, k):
    que = deque()
    que.append((y, x))
    flag = False
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = (x + dx[i]) % m
            if ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == k:
                graph[ny][nx] = 0
                flag = True
                que.append((ny, nx))
    return flag


def get_average():
    cnt = 0
    s = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] > 0:
                cnt += 1
                s += graph[y][x]
    return s / cnt if cnt > 0 else -1


n, m, t = map(int, si().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, m - 1, 1]
graph = [deque(list(map(int, si().split()))) for _ in range(n)]
order = []
for _ in range(t):
    p, d, k = map(int, si().split())
    if d == 0:
        order.append((p, k))
    else:
        order.append((p, -k))

for p, q in order:
    chk = False
    rotate(p, q)
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                if bfs(i, j, graph[i][j]):
                    chk = True
    if not chk:
        ave = get_average()
        if ave > -1:
            for i in range(n):
                for j in range(m):
                    if graph[i][j] > 0:
                        if graph[i][j] > ave:
                            graph[i][j] -= 1
                        elif graph[i][j] < ave:
                            graph[i][j] += 1

res = 0
for i in range(n):
    res += reduce(lambda acc, cur: acc + cur, graph[i], 0)
print(res)
