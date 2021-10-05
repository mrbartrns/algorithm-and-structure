# BOJ 6087 레이저 통신
import heapq
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def get_sp_and_ep(graph):
    ret = []
    for y in range(H):
        for x in range(W):
            if graph[y][x] == "C":
                ret.append((y, x))
    return ret


def bfs(sy, sx, sd, board):
    q = []
    distance[sy][sx] = 0
    # q.append((sy, sx, sd, 0))
    heapq.heappush(q, (0, sy, sx, sd))
    while q:
        # y, x, d, cnt = q.popleft()
        cnt, y, x, d = heapq.heappop(q)

        if cnt > distance[y][x]:
            continue

        if y == ey and x == ex:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue

            if board[ny][nx] == "*":
                continue

            value = cnt
            if i != d:
                value += 1

            if distance[ny][nx] >= value:
                distance[ny][nx] = value
                # q.append((ny, nx, i, value))
                heapq.heappush(q, (value, ny, nx, i))


W, H = map(int, si().split(" "))
graph = [list(si().strip()) for _ in range(H)]
distance = [[INF for _ in range(W)] for _ in range(H)]
cpoint = get_sp_and_ep(graph)
sy, sx = cpoint[0]
ey, ex = cpoint[1]
distance[sy][sx] = 0
for i in range(4):
    ny = sy + dy[i]
    nx = sx + dx[i]
    if ny < 0 or ny >= H or nx < 0 or nx >= W:
        continue
    if graph[ny][nx] != "*":
        bfs(ny, nx, i, graph)

print(distance[ey][ex])
