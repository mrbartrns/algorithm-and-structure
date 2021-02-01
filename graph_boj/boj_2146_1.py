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
        graph[x][y] = label
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, label)
        return True

    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j, label):
            label += 1


def bfs(label):
    cnt = 0
    que = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == label:
                que.append((i, j))
                visited[i][j] = True
    while que:
        size = len(que)
        for _ in range(size):
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if graph[nx][ny] != 0 and graph[nx][ny] != label:
                    return cnt
                elif graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))
        cnt += 1  # 하나의 점이 아닌 영역으로부터 퍼져나간다고 생각
    return cnt


res = 10000
for i in range(1, label):
    visited = [[False for _ in range(n)] for _ in range(n)]
    res = min(res, bfs(i))

print(res)