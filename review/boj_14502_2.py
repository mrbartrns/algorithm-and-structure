# BOJ 14502 (연구소)
import copy
import sys
from collections import deque
from itertools import combinations

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(que: deque) -> None:
    """
    do breadth first searching and spread viruses.
    Args:
        que(deque): queue of virus locations list

    Returns: None

    """
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if maps[ny][nx] == 1:
                continue

            if maps[ny][nx] == 0:
                maps[ny][nx] = 2
                que.append((ny, nx))


def get_safe_area():
    """
    count safe area on the graph(maps).
    Returns(int): number of zero on the graph

    """
    cnt = 0
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 0:
                cnt += 1
    return cnt


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
temp = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]

viruses = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            viruses.append((i, j))

zeros = list(combinations(temp, 3))
res = 0
for zero_locations in zeros:
    maps = copy.deepcopy(graph)
    queue = deque(viruses)
    for r, c in zero_locations:
        maps[r][c] = 1

    bfs(queue)
    res = max(res, get_safe_area())
print(res)
