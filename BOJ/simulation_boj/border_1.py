# BOJ 16234
import sys
from collections import deque

si = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    que = deque()
    que.append((x, y))
    s = graph[x][y]
    labels[x][y] = label
    block = 1
    visited[x][y] = True
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                changed[0] = True
                visited[nx][ny] = True
                que.append((nx, ny))
                s += graph[nx][ny]
                block += 1
                labels[nx][ny] = label
    avg = s // block
    return label, avg


# n, L, R = map(int, si().split())
# graph = [list(map(int, si().split())) for _ in range(n)]
n, L, R = 50, 10, 60
graph = [
    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80,
     90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] for _ in range(50)]
cnt = 0

while True:
    changed = [False]
    visited = [[False for _ in range(n)] for _ in range(n)]
    label = 1
    labels = [[0 for _ in range(n)] for _ in range(n)]
    label_values = [0] * 50000

    # 조건에 맞는 인접 영역 탐색하기
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                current_label, average = bfs(i, j)
                label_values[current_label] = average
                label += 1
    if not changed[0]:
        break

    # label 값에 따라 그래프 내부 값 초기화하기
    for i in range(n):
        for j in range(n):
            graph[i][j] = label_values[labels[i][j]]

    cnt += 1

# 더이상 될 수 없을때 까지 반복하기
# for y in range(n):
#     print(" ".join(list(map(str, labels[y]))))
print(cnt)
