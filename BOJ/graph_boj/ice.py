# BOJ 2573 빙산
from collections import deque
import sys

sys.setrecursionlimit(100000)
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# def dfs(y, x, visited, label_number):
#     if y < 0 or y >= N or x < 0 or x >= M:
#         return False

#     if graph[y][x] == 0:
#         return False

#     if not visited[y][x]:
#         visited[y][x] = label_number
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             dfs(ny, nx, visited, label_number)
#         return True

#     return False
def bfs(sy, sx, label_number, visited):
    que = deque()
    visited[sy][sx] = label_number
    que.append((sy, sx))
    while que:
        y, x = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if graph[ny][nx] == 0:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = label_number
                que.append((ny, nx))


def check_ice():
    for y in range(N):
        for x in range(M):
            if graph[y][x] > 0:
                return False
    return True


def substrate():
    for y in range(N):
        for x in range(M):
            graph[y][x] = (
                0 if graph[y][x] - info[y][x] < 0 else graph[y][x] - info[y][x]
            )


def check_sea():
    """주변에 바다가 있는지 확인하는 함수"""
    for y in range(N):
        for x in range(M):
            if graph[y][x] > 0:
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= N or nx < 0 or nx >= M:
                        continue
                    if graph[ny][nx] == 0:
                        info[y][x] += 1


def paint_label():
    label_number = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    """라벨 표시 함수"""
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, label_number, visited)
                label_number += 1
    return label_number


N, M = map(int, si().split(" "))
graph = [list(map(int, si().split(" "))) for _ in range(N)]
cnt = 0
while True:
    # check label
    info = [[0 for _ in range(M)] for _ in range(N)]
    label_number = paint_label()
    if label_number >= 3:
        print(cnt)
        break
    else:
        if check_ice():
            print(0)
            break
    check_sea()
    substrate()
    cnt += 1
