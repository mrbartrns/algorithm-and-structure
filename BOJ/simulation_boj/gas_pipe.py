# BOJ 2931
import copy
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

pipes = {
    "|": [0, 1, -1, -1],
    "-": [-1, -1, 2, 3],
    "1": [3, -1, 1, -1],
    "2": [-1, 3, 0, -1],
    "3": [-1, 2, -1, 0],
    "4": [2, -1, -1, 1],
    "+": [0, 1, 2, 3],
}


def bfs(y, x, maps, new_pipe, route_cnt, d):
    cnt = 2
    que = deque()
    if point < 4:
        new_pipe_y = -1
        new_pipe_x = -1
    else:
        new_pipe_y = my
        new_pipe_x = mx

    que.append((y, x, d))
    while que:
        y, x, d = que.popleft()

        # 다음 좌표로 이동
        ny = y + dy[d]
        nx = x + dx[d]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            return -1, -1

        if maps[ny][nx] == "M" or maps[ny][nx] == "Z":
            if maps[ny][nx] == "M":
                return -1, -1
            if maps[ny][nx] == "Z":
                cnt += 1
                if cnt < route_cnt:
                    return -1, -1
                return new_pipe_y, new_pipe_x

        elif maps[ny][nx] == ".":
            maps[ny][nx] = new_pipe
            if pipes[new_pipe][d] == -1:
                return -1, -1
            new_pipe_y = ny
            new_pipe_x = nx
            que.append((ny, nx, pipes[new_pipe][d]))
            cnt += 1
        else:
            next_pipe = maps[ny][nx]
            if pipes[next_pipe][d] == -1:
                return -1, -1
            que.append((ny, nx, pipes[next_pipe][d]))
            cnt += 1

    return -1, -1


n, m = map(int, si().split())
graph = [list(si().strip()) for _ in range(n)]
sy, sx = -1, -1
routes = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == "M":
            sy, sx = i, j
        if graph[i][j] != ".":
            routes += 1
routes += 1
for pipe in pipes:
    copied_graph = copy.deepcopy(graph)
    point = 0
    ret_y, ret_x = -1, -1
    ans = False
    # M 주변이 모두 "."인지 확인하기
    for i in range(4):
        my = sy + dy[i]
        mx = sx + dx[i]
        if my < 0 or my >= n or mx < 0 or mx >= m:
            point += 1
            continue
        if copied_graph[my][mx] == "." or copied_graph[my][mx] == "Z":
            point += 1
        else:
            n_pipe = copied_graph[my][mx]
            if pipes[n_pipe][i] == -1:
                point += 1
                continue
            else:
                direction = pipes[n_pipe][i]
                ret_y, ret_x = bfs(my, mx, copied_graph, pipe, routes, direction)
                if ret_y > -1 and ret_x > -1:
                    ans = True
                    print(ret_y + 1, ret_x + 1, pipe)
                    break
    if ans:
        break

    # M 주변이 모두 "."일때(바로 갈 수 있는 루트가 없을 때)
    if point == 4:
        print("here")
        for i in range(4):
            my = sy + dy[i]
            mx = sx + dx[i]
            if my < 0 or my >= n or mx < 0 or mx >= m:
                continue
            if copied_graph[my][mx] != "." and pipes[copied_graph[my][mx]][i] == -1:
                continue
            copied_graph[my][mx] = pipe
            direction = pipes[pipe][i]
            if pipes[pipe][i] > -1:
                ret_y, ret_x = bfs(my, mx, copied_graph, pipe, routes, direction)
                if ret_y > -1 and ret_x > -1:
                    print(ret_y + 1, ret_x + 1, pipe)
                    ans = True
                    break
            copied_graph[my][mx] = "."

    if ans:
        break
