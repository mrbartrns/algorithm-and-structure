import copy
import sys
from collections import deque
from itertools import combinations

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def safe_area(maps):
    cnt = 0
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 0:
                cnt += 1
    return cnt


def bfs(queue, maps):
    for y, x in queue:
        visited[y][x] = True
    que = deque(queue)
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if not visited[ny][nx] and maps[ny][nx] == 0:
                visited[ny][nx] = True
                maps[ny][nx] = 2
                que.append((ny, nx))


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
zeros = []
viruses = deque()
area = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zeros.append((i, j))
        elif graph[i][j] == 2:
            viruses.append((i, j))
locations = list(combinations(zeros, 3))
for i in range(len(locations)):
    copied_maps = copy.deepcopy(graph)
    visited = [[False for _ in range(m)] for _ in range(n)]
    for j in range(3):
        r, c = locations[i][j]
        copied_maps[r][c] = 1
    bfs(viruses, copied_maps)
    area = max(area, safe_area(copied_maps))
print(area)
