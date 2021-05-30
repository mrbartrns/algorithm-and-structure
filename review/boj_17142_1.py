# BOJ 17142 (연구소3)
import sys
from collections import deque
from itertools import combinations

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def bfs(que):
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if graph[ny][nx] == 1:
                continue

            if maps[ny][nx] == -1:
                maps[ny][nx] = maps[y][x] + 1
                que.append((ny, nx))


def has_chosen():
    for y in range(n):
        for x in range(n):
            if graph[y][x] != 1 and maps[y][x] == -1:
                return False
    return True


n, m = map(int, si().split())
loc = []  # all locations of viruses
graph = [list(map(int, si().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            loc.append((i, j))

res = INF
chk = False
# 조합
viruses = list(combinations(loc, m))
for location in viruses:
    maps = [[-1 for _ in range(n)] for _ in range(n)]  # 총 카운트 표시하는 2차원 배열
    queue = deque()
    for r, c in location:
        maps[r][c] = 0
        queue.append((r, c))
    bfs(queue)
    temp = 0
    if has_chosen():
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 0:
                    temp = max(temp, maps[i][j])

        res = min(res, temp)
print(res if res < INF else -1)
