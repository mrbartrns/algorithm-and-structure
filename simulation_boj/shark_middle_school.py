# BOJ 21609
import heapq
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy, sx, label_number, color):
    que = deque()
    block = 0
    rainbow_block = 0
    que.append((sy, sx))
    visited[sy][sx] = label_number
    block += 1
    while que:
        y, x = que.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if graph[ny][nx] == -1:
                continue
            if visited[ny][nx] == -1:
                if graph[ny][nx] == 0 or graph[ny][nx] == color:
                    visited[ny][nx] = label_number
                    que.append((ny, nx))
                    if graph[ny][nx] == 0:
                        rainbow_block += 1
                    else:
                        block += 1
    if rainbow_block + block >= 2:
        heapq.heappush(q, (-(rainbow_block + block), -rainbow_block, -block, -sy, -sx, label_number))


# 디버그 1순위
def gravity():
    for x in range(n):
        for y in range(n):
            if graph[y][x] == -2:
                for k in range(y, 0, -1):
                    if graph[k - 1][x] == -1:
                        break
                    graph[k][x], graph[k - 1][x] = graph[k - 1][x], graph[k][x]


def rotate(maps):
    new_maps = []
    for x in range(n - 1, -1, -1):
        new_row = []
        for y in range(n):
            new_row.append(maps[y][x])
        new_maps.append(new_row)
    return new_maps


def print_graph(maps):
    for y in range(n):
        print(maps[y])
    print()


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
score = 0
while True:
    q = []
    ln = 0
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    # bfs 실행하기
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] > 0:
                bfs(i, j, ln, graph[i][j])
                ln += 1
    if q:
        print(q)
        s, _, _, _, _, label = heapq.heappop(q)
        s = abs(s)
        score += s ** 2
        # 블록 지우기
        for i in range(n):
            for j in range(n):
                if visited[i][j] == label:
                    graph[i][j] = -2
        gravity()
        graph = rotate(graph)
        gravity()
    else:
        break

print(score)
