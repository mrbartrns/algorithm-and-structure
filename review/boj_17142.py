# BOJ 17142 (연구소 3)
import sys
from collections import deque
from itertools import combinations

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def bfs(que: deque) -> None:
    """
    do breadth first searching on the graph and map.
    Args:
        que(deque): locations of viruses

    Returns: None

    """
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
graph = [list(map(int, si().split())) for _ in range(n)]
av = []
blanks = 0
res = INF

# 바이러스 위치 추가 및 공백의 갯수 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] != 1:
            blanks += 1
        if graph[i][j] == 2:
            av.append((i, j))

viruses = list(combinations(av, m))

for locations in viruses:
    maps = [[-1 for _ in range(n)] for _ in range(n)]
    queue = deque()
    for r, c in locations:
        maps[r][c] = 0
        queue.append((r, c))
    bfs(queue)
    if has_chosen():
        cnt = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 0:
                    cnt = max(cnt, maps[i][j])
        res = min(res, cnt)

print(res if res < INF else -1)
