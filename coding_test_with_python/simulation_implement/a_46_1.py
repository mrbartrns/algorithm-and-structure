# BOJ 16236 (아기상어)
import heapq
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x, size):
    que = deque()
    q = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[y][x] = True
    que.append((y, x, 0))
    while que:
        y, x, cnt = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if graph[ny][nx] > size:
                continue

            if not visited[ny][nx] and graph[ny][nx] <= size:
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))
                if 0 < graph[ny][nx] < size:
                    heapq.heappush(q, (cnt + 1, ny, nx))

    if q:
        return heapq.heappop(q)
    else:
        return 0, 0, 0


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
baby_shark = [0, 0, 2]
cnt = 0
time = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            baby_shark[0], baby_shark[1] = i, j

while True:
    t, next_y, next_x = bfs(baby_shark[0], baby_shark[1], baby_shark[2])
    if t == 0:
        print(time)
        break

    cur_y, cur_x = baby_shark[0], baby_shark[1]
    graph[cur_y][cur_x] = 0
    graph[next_y][next_x] = 9
    baby_shark[0], baby_shark[1] = next_y, next_x
    cnt += 1
    time += t
    if cnt == baby_shark[2]:
        baby_shark[2] += 1
        cnt = 0
