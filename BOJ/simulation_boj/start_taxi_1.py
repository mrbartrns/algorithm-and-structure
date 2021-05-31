# BOJ 19238
import heapq
import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
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
            heapq.heappush(ret, (cnt, y, x))
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
    if ret:
        cnt, y, x = heapq.heappop(ret)
        return y, x, cnt
    else:
        return -1, -1, -1


def move_taxi(y, x, p):
    que = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    que.append((y, x, 0))
    visited[y][x] = True
    while que:
        y, x, cnt = que.popleft()
        if p in destination[y][x]:
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


def check(y, x, fuel_counts):
    if y == -1 and x == -1 and fuel_counts == -1:
        return False
    return True


n, m, f = map(int, si().split())
m_cnt = m
graph = [list(map(int, si().split())) for _ in range(n)]
passenger = [[0 for _ in range(n)] for _ in range(n)]
destination = [[set() for _ in range(n)] for _ in range(n)]
sr, sc = map(int, si().split())
start_r = sr - 1
start_c = sc - 1
for i in range(m):
    r1, c1, r2, c2 = map(int, si().split())
    passenger[r1 - 1][c1 - 1] = i + 1
    destination[r2 - 1][c2 - 1].add(i + 1)


r, c = start_r, start_c
fuel = f
flag = True
while m_cnt > 0:
    tr, tc, cnt1 = search_passenger(r, c)
    if not check(tr, tc, cnt1):
        flag = False
        break
    p_num = passenger[tr][tc]

    if fuel <= cnt1:
        flag = False
        break
    fuel -= cnt1

    r, c, cur_fuel = move_taxi(tr, tc, p_num)
    if not check(r, c, cur_fuel):
        flag = False
        break

    passenger[tr][tc] = 0
    destination[r][c].remove(p_num)

    if cur_fuel > fuel:
        flag = False
        break

    fuel -= cur_fuel
    fuel += cur_fuel * 2
    m_cnt -= 1

print(fuel if flag else -1)
