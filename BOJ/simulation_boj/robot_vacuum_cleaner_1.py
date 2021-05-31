# BOJ 14503
import sys

si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solve(i, j, d):
    x, y = i, j
    direction = d
    cnt = 0

    while True:
        flag = 0
        if not visited[x][y]:
            visited[x][y] = True
            cnt += 1
        while flag < 4:
            direction = (direction + 3) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]

            if graph[nx][ny] == 0 and not visited[nx][ny]:
                x, y = nx, ny  # direction은 이미 저장되어 있는 상태
                break

            flag += 1

        if flag == 4:
            if direction == 0 and x + 1 < n and graph[x + 1][y] == 0:
                x, y = x + 1, y
            elif direction == 1 and y - 1 >= 0 and graph[x][y - 1] == 0:
                x, y = x, y - 1
            elif direction == 2 and x - 1 >= 0 and graph[x - 1][y] == 0:
                x, y = x - 1, y
            elif direction == 3 and y + 1 < m and graph[x][y + 1] == 0:
                x, y = x, y + 1
            else:
                return cnt


n, m = map(int, si().split())
x, y, d = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
"""
n, m = 11, 10
graph = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
x, y, d = 7, 4, 0
"""
visited = [[False for _ in range(m)] for _ in range(n)]
print(solve(x, y, d))