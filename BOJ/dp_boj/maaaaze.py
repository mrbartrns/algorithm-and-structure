from collections import deque
import copy
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321
dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]


def dijkstra(sz, sy, sx, maps):
    q = deque()
    visited = [[[False for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[sz][sy][sx] = True
    q.append((0, sz, sy, sx))
    while q:
        cnt, z, y, x = q.popleft()
        if z == 4 and y == 4 and x == 4:
            return cnt
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if nz < 0 or nz >= 5 or ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue
            if maps[nz][ny][nx] == 0:
                continue
            if not visited[nz][ny][nx]:
                visited[nz][ny][nx] = True
                q.append((cnt + 1, nz, ny, nx))
    return INF


def rotate(maps):
    ret = []
    for j in range(5):
        row = []
        for i in range(4, -1, -1):
            row.append(maps[i][j])
        ret.append(row)
    return ret


def make_maze():
    ret = []
    for i in range(5):
        idx = order[i]
        turn = rotates[i]
        maps = copy.deepcopy(adj[idx])
        for _ in range(turn):
            maps = rotate(maps)
        ret.append(maps)
    return ret


def backtrack_rotation(idx):
    if idx == 5:
        maps = make_maze()
        if maps[0][0][0] == 0 or maps[4][4][4] == 0:
            return
        answer[0] = min(answer[0], dijkstra(0, 0, 0, maps))
        return
    for i in range(4):
        rotates.append(i)
        backtrack_rotation(idx + 1)
        rotates.pop()


def backtrack_order(idx, visited):
    if idx == 5:
        backtrack_rotation(0)
        return
    for i in range(5):
        if (1 << i) & visited:
            continue
        visited = (1 << i) | visited
        order.append(i)
        backtrack_order(idx + 1, visited)
        order.pop()
        visited = (1 << i) ^ visited


adj = []
for _ in range(5):
    graph = [list(map(int, si().split(" "))) for _ in range(5)]
    adj.append(graph)
order = []
rotates = []
answer = [INF]
backtrack_order(0, 0)
print(answer[0] if answer[0] < INF else -1)
