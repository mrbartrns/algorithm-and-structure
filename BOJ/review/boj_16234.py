# BOJ 16234 (인구 이동)
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x, label):
    que = deque([(y, x)])
    visited[y][x] = True
    labels[y][x] = label
    change = False
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if not visited[ny][nx] and L <= abs(graph[ny][nx] - graph[y][x]) <= R:
                visited[ny][nx] = True
                labels[ny][nx] = label
                change = True
                que.append((ny, nx))
    return change


def refresh():
    for i in range(N):
        for j in range(N):
            cur_label = labels[i][j]
            cur_val = populations[cur_label] // countries[cur_label]
            graph[i][j] = cur_val


N, L, R = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(N)]
cnt = 0

while True:
    label_number = 1
    labels = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    done = True
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                is_changed = bfs(i, j, label_number)
                label_number += 1
                if is_changed:
                    done = False
    if done:
        break

    countries = [0] * (label_number + 1)
    populations = [0] * (label_number + 1)
    for i in range(N):
        for j in range(N):
            cur_label = labels[i][j]
            countries[cur_label] += 1
            populations[cur_label] += graph[i][j]
    refresh()
    cnt += 1

print(cnt)
