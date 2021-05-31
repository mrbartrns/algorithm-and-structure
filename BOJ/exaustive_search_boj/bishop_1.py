# BOJ 1799
import copy
import sys

si = sys.stdin.readline
dy = [-1, 1, -1, 1]
dx = [-1, 1, 1, -1]


def backtrack(idx, maps):
    if idx == len(s_point):
        return
    for i in range(len(s_point)):
        y, x = s_point[i]
        cp = copy.deepcopy(maps)
        if not cp[y][x]:
            cp[y][x] = True
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                while True:
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        break
                    cp[ny][nx] = True
                    ny += dy[d]
                    nx += dx[d]
            max_value[0] = max(max_value[0], idx + 1)
            backtrack(idx + 1, cp)


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
# n = 5
# graph = [
#     [1, 1, 0, 1, 1],
#     [0, 1, 0, 0, 0],
#     [1, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0],
#     [1, 0, 1, 1, 1],
# ]
visited = [[False for _ in range(n)] for _ in range(n)]
s_point = []
max_value = [0]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            s_point.append((i, j))
backtrack(0, visited)
print(max_value[0])
