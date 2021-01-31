# BOJ 7576
import sys
from collections import deque


def bfs(que):
    cnt = 0
    while que:
        x, y = que.popleft()
        visited[x][y] = True  # visited x, y가 없어도 가능
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if arr[nx][ny] == -1:
                continue

            if arr[nx][ny] == 0 and not visited[nx][ny]:
                arr[nx][ny] = arr[x][y] + 1
                if cnt < arr[nx][ny]:
                    cnt = arr[nx][ny]
                visited[nx][ny] = True
                que.append((nx, ny))

    return cnt


si = sys.stdin.readline

m, n = map(int, si().split())
arr = []
que = deque()
zero = False
for i in range(n):
    temp = list(map(int, si().split()))
    arr.append(temp)
    for j in range(m):
        if temp[j] == 1:
            que.append((i, j))
        elif temp[j] == 0:
            zero = True

if not zero:
    print(0)
    sys.exit(0)

visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
val = bfs(que) - 1
done = True
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            done = False
            break

if done:
    print(val)
else:
    print(-1)
