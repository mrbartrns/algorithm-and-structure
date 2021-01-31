# BOJ 7576
from collections import deque

n = 4
m = 6

graph = [[0 for _ in range(m)] for _ in range(n)]
graph[n - 1][m - 1] = 1

# 토마토는 어디에서나 존재할 수 있고, -1로 둘러쌓인 곳은 지나갈 수 없다. 없는 토마토 자리이다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 그래프 내의 1인 좌표 삽입하기
que = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append((i, j))


def bfs(que):
    cnt = 0
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                if graph[nx][ny] > cnt:
                    cnt = graph[nx][ny]
                que.append((nx, ny))
    return cnt


zero = False
val = bfs(que) - 1  # 1을 빼주는 이유는 처음에 1부터 시작했기 때문
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero = True
            break
print(val if not zero else -1)
