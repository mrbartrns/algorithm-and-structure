# BOJ 1600 말이 되고픈 원숭이
from collections import deque
import sys


sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
hy = [-2, -1, 1, 2, 2, 1, -1, -2]
hx = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs():
    """원숭이의 움직임을 계산하는 함수"""
    que = deque()
    visited = [[[False for _ in range(W)] for _ in range(H)] for _ in range(31)]
    visited[K][0][0] = True
    que.append((0, 0, K, 0)) # y, x, k, cnt
    while que:
        y, x, k, cnt = que.popleft()
        if y == H - 1 and x == W - 1:
            return cnt
        
        # 보통 방법으로 움직일때
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            if graph[ny][nx] == 1:
                continue
            if not visited[k][ny][nx]:
                visited[k][ny][nx] = True
                que.append((ny, nx, k, cnt + 1))
        
        # 말과 같은 방법으로 움직일 때
        if k == 0:
            continue
        for i in range(8):
            ny = y + hy[i]
            nx = x + hx[i]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            if graph[ny][nx] == 1:
                continue
            if not visited[k - 1][ny][nx]:
                visited[k - 1][ny][nx] = True
                que.append((ny, nx, k - 1, cnt + 1))
    return -1

K = int(si())
W, H = map(int, si().split(" "))
graph = [list(map(int, si().split(" "))) for _ in range(H)]
print(bfs())