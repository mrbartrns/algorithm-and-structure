# BOJ 7562
import sys
from collections import deque

si = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(n):
    que = deque()
    que.append((cur_x, cur_y, 0))
    visited[cur_x][cur_y] = True
    while que:
        x, y, cnt = que.popleft()
        if x == fin_x and y == fin_y:
            return cnt
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny, cnt + 1))


t = int(si())
for _ in range(t):
    size = int(si())
    visited = [[False for _ in range(size)] for _ in range(size)]
    cur_x, cur_y = map(int, si().split())
    fin_x, fin_y = map(int, si().split())
    print(bfs(size))