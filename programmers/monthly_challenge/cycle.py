# 빛의 경로 사이클
from collections import deque


def bfs(sy, sx, sd, row, col, grid, visited):
    que = deque()
    dy = [row - 1, 0, 1, 0]
    dx = [0, col - 1, 0, 1]
    que.append((sy, sx, sd, 0))
    while que:
        y, x, d, cnt = que.popleft()

        if grid[y][x] == "S":
            nd = d
            ny = (y + dy[nd]) % row
            nx = (x + dx[nd]) % col

        elif grid[y][x] == "L":
            nd = (d + 1) % 4
            ny = (y + dy[nd]) % row
            nx = (x + dx[nd]) % col

        else:
            nd = (d + 3) % 4
            ny = (y + dy[nd]) % row
            nx = (x + dx[nd]) % col

        if not visited[ny][nx][nd]:
            visited[ny][nx][nd] = cnt + 1
            que.append((ny, nx, nd, cnt + 1))


def solution(grid):
    answer = []
    row = len(grid)
    col = len(grid[0])
    visited = [[[0 for _ in range(4)] for _ in range(col)] for _ in range(row)]
    for y in range(row):
        for x in range(col):
            for i in range(4):
                if not visited[y][x][i]:
                    bfs(y, x, i, row, col, grid, visited)
                    answer.append(visited[y][x][i])
    answer.sort()
    return answer


if __name__ == "__main__":
    grid = ["R", "R"]
    print(solution(grid))