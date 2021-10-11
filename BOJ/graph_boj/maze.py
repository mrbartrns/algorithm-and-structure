# BOJ 14923
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(hy, hx, ey, ex):
    """미로를 탈출하는데 필요한 최소 거리를 탐색하는 함수"""
    que = deque()
    visited[1][hy][hx] = True
    que.append((hy, hx, 1, 0))  # y, x, e, cnt
    while que:
        y, x, e, cnt = que.popleft()

        if y == ey and x == ex:
            return cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if graph[ny][nx] == 0 and not visited[e][ny][nx]:
                visited[e][ny][nx] = True
                que.append((ny, nx, e, cnt + 1))

            elif graph[ny][nx] == 1 and e == 1 and not visited[1 - e][ny][nx]:
                visited[1 - e][ny][nx] = True
                que.append((ny, nx, 1 - e, cnt + 1))
    return -1


N, M = map(int, si().split(" "))
HY, HX = map(int, si().split(" "))
EY, EX = map(int, si().split(" "))
HY, HX = HY - 1, HX - 1
EY, EX = EY - 1, EX - 1
graph = [list(map(int, si().split(" "))) for _ in range(N)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]

answer = bfs(HY, HX, EY, EX)
print(answer)
