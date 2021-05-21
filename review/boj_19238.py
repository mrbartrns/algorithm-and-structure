# BOJ 19238  (스타트 택시)
import heapq
import sys
from collections import deque

si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x):
    que = deque()
    visited = [[0 for _ in range(n)] for _ in range(n)]
    que.append((y, x, 0))
    visited[y][x] = True
    q = []
    while que:
        y, x, cnt = que.popleft()
        if people[y][x] > 0:
            heapq.heappush(q, (cnt, y, x, people[y][x]))

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
    if q:
        cnt, y, x, idx = heapq.heappop(q)
        people[y][x] = 0
        return y, x, cnt, idx
    return -1, -1, -1, -1


def go(y, x, k):
    que = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[y][x] = True
    que.append((y, x, 0))
    while que:
        y, x, cnt = que.popleft()
        if k in destination[y][x]:
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


n, m, fuel = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
people = [[0 for _ in range(n)] for _ in range(n)]
destination = [[set() for _ in range(n)] for _ in range(n)]
chk = False
left = m

start_y, start_x = map(int, si().split())
start_y -= 1
start_x -= 1
label_number = 1
for _ in range(m):
    a, b, c, d = map(int, si().split())
    people[a - 1][b - 1] = label_number
    destination[c - 1][d - 1].add(label_number)
    label_number += 1

while True:
    if not left:
        chk = True
        break
    start_y, start_x, counts, person = bfs(start_y, start_x)
    if start_y == -1 and start_x == -1 and counts == -1 and person == -1:
        print(-1)
        break
    else:
        left -= 1

    if fuel - counts <= 0:
        print(-1)
        break
    fuel -= counts

    start_y, start_x, s = go(start_y, start_x, person)
    if start_y == -1 and start_x == -1 and s == -1:
        print(-1)
        break

    if fuel - s < 0:
        print(-1)
        break

    fuel -= s
    fuel += 2 * s

if chk:
    print(fuel)
