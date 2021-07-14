# BOJ 14502 (연구소)
import copy
import sys
from collections import deque
from itertools import combinations

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(que, board):
    while que:
        y, x = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if board[ny][nx] == 0:
                board[ny][nx] = 1
                que.append((ny, nx))


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
zeros = []
viruses = deque()
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zeros.append((i, j))
        elif graph[i][j] == 2:
            viruses.append((i, j))

comb = combinations(zeros, 3)

for new_walls in comb:
    maps = copy.deepcopy(graph)
    copied_viruses = copy.deepcopy(viruses)
    for i, j in new_walls:
        maps[i][j] = 1
    bfs(copied_viruses, maps)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                cnt += 1
    answer = max(answer, cnt)
print(answer)
