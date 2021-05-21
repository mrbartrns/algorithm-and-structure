# BOJ 16234 (국경이동)
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x, k):
    que = deque()
    que.append((y, x))
    label[y][x] = k
    flag = False
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if label[ny][nx] == -1 and L <= abs(graph[ny][nx] - graph[y][x]) <= R:
                label[ny][nx] = k
                que.append((ny, nx))
                flag = True
    return flag


n, L, R = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
time = 0

while True:
    chk = False
    label = [[-1 for _ in range(n)] for _ in range(n)]
    label_number = 0
    for i in range(n):
        for j in range(n):
            if label[i][j] == -1:
                if bfs(i, j, label_number):
                    chk = True
                label_number += 1
    if not chk:
        break
    population = [0] * (label_number)
    counts = [0] * (label_number)
    for i in range(n):
        for j in range(n):
            idx = label[i][j]
            population[idx] += graph[i][j]
            counts[idx] += 1
    new_ = [population[i] // counts[i] for i in range(label_number)]
    for i in range(n):
        for j in range(n):
            graph[i][j] = new_[label[i][j]]
    time += 1
print(time)
