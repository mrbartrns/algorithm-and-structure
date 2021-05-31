# BOJ 2933
import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321

# sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

n, m = map(int, si().split())
graph = [list(si().strip()) for _ in range(n)]
t = int(si())
heights = list(map(lambda el: n - el, list(map(int, si().split()))))


# 막대 던지기 함수
def throw_stick(throw_height: int, idx: int):
    if idx % 2 == 0:
        for i in range(m):
            if graph[throw_height][i] == "x":
                graph[throw_height][i] = "."
                return True
    else:
        for i in range(m - 1, -1, -1):
            if graph[throw_height][i] == "x":
                graph[throw_height][i] = "."
                return True
    return False


# 바닥에 붙어있는 클러스터들을 True 처리해주기
def bfs(y, x):
    que = deque()
    visited[y][x] = True
    que.append((y, x))
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if graph[ny][nx] == "x" and not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx))


def remake_map():
    h = INF
    size = len(air_cluster)
    for i in range(size):
        y, x = air_cluster[i]
        h = min(h, gravity(y, x))
    air_cluster.sort(key=lambda e: (-e[0]))
    for i in range(size):
        y, x = air_cluster[i]
        graph[y][x] = "."
        graph[y + h][x] = "x"


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


for tc in range(len(heights)):
    visited = [[False for _ in range(m)] for _ in range(n)]
    cluster = [[False for _ in range(m)] for _ in range(n)]
    air_cluster = []

    if not throw_stick(heights[tc], tc):
        continue

    for i in range(m):
        if graph[n - 1][i] == "x" and not visited[n - 1][i]:
            bfs(n - 1, i)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == "x" and not visited[i][j]:
                air_cluster.append((i, j))
                cluster[i][j] = True

    remake_map()
for i in range(n):
    print("".join(graph[i]))
