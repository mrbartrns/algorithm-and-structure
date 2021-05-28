# BOJ 20609 (상어 중학교)
import heapq
import sys
from collections import deque

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]


def gravity(maps):
    for x in range(n):
        for y in range(n):
            if maps[y][x] == -2:
                for k in range(y, 0, -1):
                    if maps[k - 1][x] == -1:
                        break
                    maps[k][x], maps[k - 1][x] = maps[k - 1][x], maps[k][x]


def rotate(maps):
    ret = []
    for x in range(n - 1, -1, -1):
        temp = []
        for y in range(n):
            temp.append(maps[y][x])
        ret.append(temp)
    return ret


def bfs(sy, sx, k):
    que = deque()
    y, x = sy, sx
    visited[y][x] = True
    que.append((y, x))
    color_block = 1
    rainbow_block = 0
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if graph[ny][nx] == -1:
                continue

            if not visited[ny][nx] and graph[ny][nx] == k:
                visited[ny][nx] = True
                que.append((ny, nx))
                color_block += 1
            elif not rainbow_visited[ny][nx] and graph[ny][nx] == 0:
                rainbow_visited[ny][nx] = True
                rainbow_block += 1
                que.append((ny, nx))
    return color_block + rainbow_block, rainbow_block


def remove():
    for i in range(n):
        for j in range(n):
            if visited[i][j] or rainbow_visited[i][j]:
                graph[i][j] = -2


def print_graph():
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=" ")
        print()
    print()


score = 0

while True:
    q = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0 and not visited[i][j]:
                rainbow_visited = [[False for _ in range(n)] for _ in range(n)]
                s_cnt, r_cnt = bfs(i, j, graph[i][j])
                if s_cnt > 1:
                    heapq.heappush(q, (-s_cnt, -r_cnt, -i, -j))
    visited = [[False for _ in range(n)] for _ in range(n)]
    if q:
        s_cnt, _, r, c = heapq.heappop(q)  # graph[r][c] is standard block
        rainbow_visited = [[False for _ in range(n)] for _ in range(n)]
        score += s_cnt ** 2
        bfs(-r, -c, graph[-r][-c])
        remove()
        gravity(graph)
        graph = rotate(graph)
        gravity(graph)
    else:
        break
print(score)
