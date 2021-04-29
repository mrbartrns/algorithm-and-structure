# BOJ 20058
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def rotate(y, x, scale, l):
    if scale == l:
        new_ = []
        for c in range(x, x + (1 << scale)):
            temp = []
            for r in range(y + (1 << scale) - 1, y - 1, -1):
                temp.append(graph[r][c])
            new_.append(temp)
        for r in range(1 << scale):
            for c in range(1 << scale):
                graph[y + r][x + c] = new_[r][c]
        return

    for i in range(2):
        for j in range(2):
            rotate(y + i * (1 << (scale - 1)), x + j * (1 << (scale - 1)), scale - 1, l)


def ice_check():
    check = [[False for _ in range(1 << n)] for _ in range(1 << n)]
    for y in range(1 << n):
        for x in range(1 << n):
            if graph[y][x] == 0:
                continue
            cnt = 4
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if ny < 0 or ny >= (1 << n) or nx < 0 or nx >= (1 << n):
                    cnt -= 1

                elif graph[ny][nx] == 0:
                    cnt -= 1

                if cnt < 3:
                    check[y][x] = True
                    break
    for y in range(1 << n):
        for x in range(1 << n):
            if check[y][x] and graph[y][x] > 0:
                graph[y][x] -= 1


def bfs(y, x):
    que = deque()
    que.append((y, x))
    visited[y][x] = True
    ret = 1
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 1 << n or nx < 0 or nx >= 1 << n:
                continue

            if not visited[ny][nx] and graph[ny][nx] > 0:
                visited[ny][nx] = True
                ret += 1
                que.append((ny, nx))
    return ret


n, q = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(1 << n)]
visited = [[False for _ in range(1 << n)] for _ in range(1 << n)]

ops = list(map(int, si().split()))
s = 0
squares = 0

for op in ops:
    rotate(0, 0, n, op)
    ice_check()

    # for i in range(1 << n):
    #     for j in range(1 << n):
    #         print(graph[i][j], end=" ")
    #     print()
    # print()

for i in range(1 << n):
    for j in range(1 << n):
        s += graph[i][j]
        if not visited[i][j] and graph[i][j] > 0:
            squares = max(squares, bfs(i, j))

print(s)
print(squares)
