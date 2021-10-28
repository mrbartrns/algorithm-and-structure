# BOJ 16197 두 동전
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    q = []
    visited = [
        [[[False for _ in range(M)] for _ in range(N)] for _ in range(M)]
        for _ in range(N)
    ]
    heapq.heappush(q, (0, sy1, sx1, sy2, sx2))
    while q:
        cnt, y1, x1, y2, x2 = heapq.heappop(q)
        if cnt > 10:
            break
        if (
            y1 < 0
            or y1 >= N
            or x1 < 0
            or x1 >= M
            or y2 < 0
            or y2 >= N
            or x2 < 0
            or x2 >= M
        ):
            return cnt

        for i in range(4):
            ny1 = y1 + dy[i]
            nx1 = x1 + dx[i]
            ny2 = y2 + dy[i]
            nx2 = x2 + dx[i]

            if (ny1 < 0 or ny1 >= N or nx1 < 0 or nx1 >= M) and (
                ny2 < 0 or ny2 >= N or nx2 < 0 or nx2 >= M
            ):
                continue
            elif (
                ny1 < 0
                or ny1 >= N
                or nx1 < 0
                or nx1 >= M
                or ny2 < 0
                or ny2 >= N
                or nx2 < 0
                or nx2 >= M
            ):
                heapq.heappush(q, (cnt + 1, ny1, nx1, ny2, nx2))
            else:
                check1 = False
                check2 = False
                if graph[ny1][nx1] == "#":
                    ny1 -= dy[i]
                    nx1 -= dx[i]
                    check1 = True
                if graph[ny2][nx2] == "#":
                    ny2 -= dy[i]
                    nx2 -= dx[i]
                    check2 = True

                if ny1 == ny2 and nx1 == nx2:
                    if check1:
                        ny2 -= dy[i]
                        nx2 -= dx[i]
                    elif check2:
                        ny1 -= dy[i]
                        nx1 -= dx[i]

                if not visited[ny1][nx1][ny2][nx2]:
                    visited[ny1][nx1][ny2][nx2] = True
                    heapq.heappush(q, (cnt + 1, ny1, nx1, ny2, nx2))
    return -1


N, M = map(int, si().split(" "))
graph = [list(si().strip()) for _ in range(N)]

sy1, sx1, sy2, sx2 = -1, -1, -1, -1
for i in range(N):
    for j in range(M):
        if graph[i][j] == "o":
            if sy1 == -1 and sx1 == -1:
                sy1, sx1 = i, j
            else:
                sy2, sx2 = i, j

print(bfs())
