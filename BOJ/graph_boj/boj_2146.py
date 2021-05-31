# BOJ 2146
from collections import deque

n = 10
graph = [
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
label = 1
visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, label):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if not visited[x][y] and graph[x][y] == 1:
        visited[x][y] = True
        graph[x][y] = label
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, label)
        return True
    return False


# 보편적으로 생각하는 연습 필요
def bfs(label):
    que = deque()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == label:
                que.append((i, j))
                visited[i][j] = True

    while que:
        size = len(que)
        for _ in range(size):  # 모든 섬 영역에 대해 탐색하기 전까지 카운트를 증가시키면 안되므로
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if graph[nx][ny] != 0 and graph[nx][ny] != label:
                    return cnt  # 다른 영역의 섬에 닫는 순간 반환
                elif graph[nx][ny] == 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = True
        cnt += 1
    return cnt


# island labeling
for i in range(n):
    for j in range(n):
        if dfs(i, j, label):
            label += 1

# sea checking
cnt = 10000
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(1, label):
    cnt = min(cnt, bfs(i))

print(cnt)