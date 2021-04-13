# BOJ 11559
import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(init_y: int, init_x: int, c: int) -> list:
    que = deque()
    vector = []
    que.append((init_y, init_x))
    visited[init_y][init_x] = True
    vector.append((init_y, init_x))
    while que:
        y, x = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny >= 12 or nx < 0 or nx >= 6:
                continue
            if not visited[ny][nx] and graph[ny][nx] == c:
                visited[ny][nx] = True
                que.append((ny, nx))
                vector.append((ny, nx))
    return vector


def has_to_remove(vector: list) -> bool:
    size = len(vector)
    flag = False
    if size >= 4:
        flag = True
        for y, x in vector:
            graph[y][x] = 0
    return flag


def block_down():
    for y in range(11, 0, -1):
        for x in range(6):
            if graph[y][x] == 0:
                for k in range(y, -1, -1):
                    if graph[k][x] > 0:
                        graph[y][x], graph[k][x] = graph[k][x], graph[y][x]
                        break


def transform(el):
    if el == ".":
        el = 0
    elif el == "R":
        el = 1
    elif el == "G":
        el = 2
    elif el == "B":
        el = 3
    elif el == "P":
        el = 4
    elif el == "Y":
        el = 5
    return el


# graph = []
# for _ in range(12):
#     temp = list(si().strip())
#     transformed = list(map(transform, temp))
#     graph.append(transformed)
graph = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 5, 0, 0, 0, 0],
         [0, 5, 2, 0, 0, 0],
         [1, 1, 5, 2, 0, 0], [1, 1, 5, 2, 2, 0]]
chain = 0
while True:
    visited = [[False for _ in range(6)] for _ in range(12)]
    passed = []
    again = False
    for i in range(12):
        for j in range(6):
            if not visited[i][j] and graph[i][j] > 0:
                passed = bfs(i, j, graph[i][j])
                if has_to_remove(passed):
                    again = True
    if not again:
        break
    block_down()
    chain += 1
    for i in range(12):
        print(" ".join(list(map(str, graph[i]))))

print(chain)
