# BOJ 19238
import sys
from collections import deque

si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def search_passenger(init_y, init_x):
    que = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    ret = []
    que.append((init_y, init_x, 0))
    visited[init_y][init_x] = True
    while que:
        y, x, cnt = que.popleft()
        if passenger[y][x] > 0:
            ret.append((y, x, cnt))
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if graph[ny][nx] == 1:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))
    ret.sort(key=lambda e: (e[2], e[0], e[1]))
    return ret[0] if ret else (-1, -1, -1)


def move_taxi(y, x, p):
    que = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    que.append((y, x, 0))
    visited[y][x] = True
    while que:
        y, x, cnt = que.popleft()
        if destination[y][x] == p:
            return y, x, cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if graph[ny][nx] == 1:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))
    return -1, -1, -1


n, m, f = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
passenger = [[0 for _ in range(n)] for _ in range(n)]
destination = [[0 for _ in range(n)] for _ in range(n)]
sr, sc = map(int, si().split())
start_r = sr - 1
start_c = sc - 1
for i in range(m):
    r1, c1, r2, c2 = map(int, si().split())
    passenger[r1 - 1][c1 - 1] = i + 1
    destination[r2 - 1][c2 - 1] = i + 1
m_cnt = m
# n, m, f = 6, 3, 15
# m_cnt = m
# graph = [[0, 0, 1, 0, 0, 0],
#          [0, 0, 1, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 1, 0],
#          [0, 0, 0, 1, 0, 0]]
# start_r, start_c = 5, 4
# passenger = [[0, 0, 0, 0, 0, 0],
#              [0, 1, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0],
#              [0, 3, 0, 0, 0, 0],
#              [0, 0, 0, 2, 0, 0],
#              [0, 0, 0, 0, 0, 0]]
# destination = [[0, 0, 0, 0, 0, 2],
#                [0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 3, 0],
#                [0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 1],
#                [0, 0, 0, 0, 0, 0]]

r, c = start_r, start_c
fuel = f
flag = True
while m_cnt > 0:
    tr, tc, cnt1 = search_passenger(r, c)
    if tr == -1 and tc == -1 and cnt1 == -1:
        flag = False
        print(-1)
        break
    p_num = passenger[tr][tc]

    if fuel <= cnt1:
        flag = False
        print(-1)
        break
    fuel -= cnt1

    r, c, cur_fuel = move_taxi(tr, tc, p_num)
    if r == -1 and c == -1 and cur_fuel == -1:
        flag = False
        print(-1)
        break

    passenger[tr][tc] = 0
    destination[r][c] = 0

    if cur_fuel > fuel:
        flag = False
        print(-1)
        break

    fuel -= cur_fuel
    fuel += cur_fuel * 2
    m_cnt -= 1

if flag:
    print(fuel)
