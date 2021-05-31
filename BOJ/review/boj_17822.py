# BOJ 17822 (원판 돌리기)
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def rotate(x, d, k):
    for i in range(x, n + 1, x):
        que = graph[i]
        if d == 0:
            que.rotate(k)
        else:
            que.rotate(-k)


def bfs(y, x, value):
    que = deque()
    visited[y][x] = True
    que.append((y, x))
    check = False
    sy, sx = y, x
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = (x + dx[i]) % m
            if ny < 1 or ny >= n + 1:
                continue
            if not visited[ny][nx] and graph[ny][nx] == value:
                visited[ny][nx] = True
                remove[ny][nx] = True
                check = True
                que.append((ny, nx))
    if check:
        remove[sy][sx] = True
    return check


def get_average():
    s = 0
    cnt = 0
    for y in range(1, n + 1):
        for x in range(m):
            if graph[y][x] > 0:
                s += graph[y][x]
                cnt += 1
    return s / cnt if cnt > 0 else -1


n, m, t = map(int, si().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, m - 1, 1]
graph = [deque([0] * m)]
score = 0
for _ in range(n):
    temp = list(map(int, si().split()))
    graph.append(deque(temp))

for _ in range(t):
    num, d, k = map(int, si().split())
    visited = [[False for _ in range(m)] for _ in range(n + 1)]
    remove = [[False for _ in range(m)] for _ in range(n + 1)]
    flag = False
    rotate(num, d, k)
    for i in range(1, n + 1):
        for j in range(m):
            if not visited[i][j] and graph[i][j] > 0:
                chk = bfs(i, j, graph[i][j])
                if chk:
                    flag = True
    if flag:
        for i in range(1, n + 1):
            for j in range(m):
                if remove[i][j]:
                    graph[i][j] = 0
    else:
        ave = get_average()
        if ave > -1:
            for i in range(1, n + 1):
                for j in range(m):
                    if 0 < graph[i][j] < ave:
                        graph[i][j] += 1
                    elif graph[i][j] > ave:
                        graph[i][j] -= 1

for i in range(1, n + 1):
    for j in range(m):
        score += graph[i][j]
print(score)
