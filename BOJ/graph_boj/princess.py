# BOJ 1941 소문난 칠공주
from collections import deque
from itertools import combinations
import sys

si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy, sx):
    q = deque()
    s_count = 0
    cnt = 1
    route[sy][sx] = False
    if adj[sy][sx] == "S":
        s_count += 1
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        if cnt == 7:
            if s_count >= 4:
                return 1
            return 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue
            if route[ny][nx]:
                route[ny][nx] = False
                q.append((ny, nx))
                if adj[ny][nx] == "S":
                    s_count += 1
                cnt += 1
    return 0


adj = [list(si().strip()) for _ in range(5)]
arr = [(i, j) for i in range(5) for j in range(5)]
comb = list(combinations(arr, 7))
answer = 0
for comb_list in comb:
    route = [[False for _ in range(5)] for _ in range(5)]
    for cy, cx in comb_list:
        route[cy][cx] = True
    answer += bfs(comb_list[0][0], comb_list[0][1])
print(answer)
