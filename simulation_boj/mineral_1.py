# BOJ 2933
import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline
INF = 987654321

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, si().split())
graph = [list(si().strip()) for _ in range(n)]
k = int(si())
heights = list(map(lambda e: n - e, list(map(int, si().split()))))


def throw_stick(h, idx):
    if idx % 2 == 0:
        for i in range(m):
            if graph[h][i] == "x":
                graph[h][i] = "."
                return True
    else:
        for i in range(m - 1, -1, -1):
            if graph[h][i] == "x":
                graph[h][i] = "."
                return True
    return False


def bfs(y, x):
    que = deque()
    que.append((y, x))
    visited[y][x] = True
    while que:
        y, x = que.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if not visited[ny][nx] and graph[ny][nx] == "x":
                visited[ny][nx] = True
                que.append((ny, nx))


def remake_map():
    min_h = INF
    size = len(air_cluster)
    for i in range(size):
        y, x = air_cluster[i]
        min_h = min(min_h, gravity(y, x))

    air_cluster.sort(key=lambda e: -e[0])
    for i in range(size):
        y, x = air_cluster[i]
        graph[y][x] = "."
        graph[y + min_h][x] = "x"


def gravity(y, x):
    cnt = 0
    for i in range(y + 1, n):
        if graph[i][x] == "x":
            if cluster[i][x]:
                return INF
            else:
                return cnt
        else:
            cnt += 1
    return cnt


for c in range(k):
    visited = [[False for _ in range(m)] for _ in range(n)]
    cluster = [[False for _ in range(m)] for _ in range(n)]
    air_cluster = []
    if not throw_stick(heights[c], c):
        continue

    # 마지막 행에 대해서만 bfs 실행
    for i in range(m):
        if not visited[n - 1][i] and graph[n - 1][i] == "x":
            bfs(n - 1, i)

    # bfs 실행후 이중반복문으로 x이면서 visited[y][x] = False 인 좌표 대입 및 cluster[y][x] = True 처리
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "x" and not visited[i][j]:
                air_cluster.append((i, j))
                cluster[i][j] = True

    remake_map()

for i in range(n):
    print("".join(graph[i]))
