# 미로 탈출

"""
n * m 크기의 직사각형 형태의 미로에 갖혔다. 미로에는 여러마리의 괴물이 있어 이를 피해 탈출해야 한다.
동빈이의 위치는 (1, 1)이며, 출구는 (n, m)이다. 한번에 한칸씩만 이동할 수 있다.
탈출하기 위한 최소 이동거리를 출력하라
"""

from collections import deque


def bfs(x, y):
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))
    return graph[n - 1][m - 1]


n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# print(graph)
print(bfs(0, 0))
