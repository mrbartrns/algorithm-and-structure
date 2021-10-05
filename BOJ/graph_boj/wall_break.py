# BOJ 14442 벽 부수고 이동하기
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    que = deque()
    que.append((0, 0, K, 1))  # y, x, k, cnt
    visited[0][0][K] = 1
    while que:
        y, x, k, cnt = que.popleft()
        if y == N - 1 and x == M - 1:
            return visited[y][x][k]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if graph[ny][nx] == "0":
                if not visited[ny][nx][k]:
                    # visited.add((ny, nx, k))
                    visited[ny][nx][k] = cnt + 1
                    que.append((ny, nx, k, cnt + 1))
            elif k > 0:
                if not visited[ny][nx][k - 1]:
                    visited[ny][nx][k - 1] = cnt + 1
                    que.append((ny, nx, k - 1, cnt + 1))
    return -1


N, M, K = map(int, si().split(" "))
graph = [list(si().strip()) for _ in range(N)]
visited = [[[0 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
print(bfs())
# print(visited[N - 1][M - 1] if visited[N - 1][M - 1] < INF else -1)
# print(visited)
