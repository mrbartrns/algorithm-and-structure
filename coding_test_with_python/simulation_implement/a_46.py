# BOJ 16236 아기 상어
from collections import deque
import sys
import heapq

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x, shark_size):
    answer = []
    que = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[y][x] = True
    que.append((y, x, 0))
    while que:
        y, x, cnt = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if graph[ny][nx] > shark_size:
                continue

            if not visited[ny][nx] and graph[ny][nx] <= shark_size:
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))
                if 0 < graph[ny][nx] < shark_size:
                    heapq.heappush(answer, (cnt + 1, ny, nx))
    if answer:
        return heapq.heappop(answer)
    else:
        return (-1, -1, -1)


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
shark_size = 2
shark_y, shark_x = 0, 0
tot = 0
eating_count = 0

# initial location of baby_shark
for i in range(n): 
    for j in range(n):
        if graph[i][j] == 9:
            shark_y = i
            shark_x = j
            break

while True:
    time, next_y, next_x = bfs(shark_y, shark_x, shark_size)

    if next_y == -1 and next_x == -1:
        break

    tot += time
    # shark_y, shark_x -> 0
    graph[shark_y][shark_x] = 0
    graph[next_y][next_x] = 9
    eating_count += 1

    # relocate shark_y, shark_x
    shark_y, shark_x = next_y, next_x

    if eating_count == shark_size:
        shark_size += 1
        eating_count = 0


print(tot)
