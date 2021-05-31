# 미로 탈출
"""
n * m 미로를 탈출하려고 하는데, 1, 1에 위치해 있으며 미로의 출구는 n, m 한번에 한칸씩 이동 가능
이동할 수 있는 미로의 최소 거리
모두 비용이 같을 때 최단거리를 구하는 방법은 bfs를 이용하는 것이다. > 모든 지점으로 이동할 수 있음
"""
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue  # for문을 한번 스킵

            if graph[nx][ny] == 0:  # 벽이므로 스킵
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))
    return graph[n - 1][m - 1]