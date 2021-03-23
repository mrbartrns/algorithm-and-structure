# BOJ 15686
import sys
from itertools import combinations

si = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
MIN = 1e12


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
chicken = []
preserved = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))

# 최대 M개라 했으므로 그 이하도 가능
for i in range(m):
    preserved.extend(list(combinations(chicken, i + 1)))

for locations in preserved:
    preset = set(locations)
    s = 0
    for i in range(n):
        for j in range(n):
            temp = 1000000000
            if graph[i][j] == 1:
                for x, y in preset:
                    temp = min(temp, abs(i - x) + abs(j - y))
                s += temp
    if MIN > s:
        MIN = s

print(MIN)


# bfs 사용시 시간 초과
"""
def bfs(i, j):
    que = deque([(i, j, 0)])
    visited[i][j] = True
    while que:
        x, y, cnt = que.popleft()
        if graph[x][y] == 2 and (x, y) in preset:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny, cnt + 1))
"""
