# 빛의 경로 사이클
from collections import deque


def bfs(sy, sx, sd, row, col, grid, route):
    s = set()
    que = deque()
    dy = [row - 1, 0, 1, 0]
    dx = [0, col - 1, 0, 1]
    if grid[sy][sx] == "S":
        nd = sd
    elif grid[sy][sx] == "L":
        nd = (sd + 1) % 4
    else:
        nd = (sd + 3) % 4
    ny = (sy + dy[nd]) % row
    nx = (sx + dx[nd]) % col
    if (ny, nx, nd) in route:
        return 0

    route.add((ny, nx, nd))
    que.append((ny, nx, nd, 1))
    while que:
        y, x, d, cnt = que.popleft()
        # print(f"y: {y} x: {x} d: {d} cnt: {cnt}")
        # if cnt > 16:
        #     break
        if y == sy and x == sx and d == sd:
            return cnt

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

        if (ny, nx, nd) in route:
            return 0
        route.add((ny, nx, nd))
        que.append((ny, nx, nd, cnt + 1))


def solution(grid):
    answer = []
    row = len(grid)
    col = len(grid[0])
    s = set()
    for y in range(row):
        for x in range(col):
            for i in range(4):
                ret = bfs(y, x, i, row, col, grid, s)
                if ret > 0:
                    answer.append(ret)
    return answer


if __name__ == "__main__":
    grid = ["SL", "LR"]
    print(solution(grid))