# BOJ 14461 소가 길을 건너간 이유 7
from collections import deque
import sys
import heapq

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def dijkstra(sy, sx):
    q = []
    distance[sy][sx] = 0
    heapq.heappush(q, (0, sy, sx))
    while q:
        dist, y, x = heapq.heappop(q)
        if distance[y][x] < dist:
            continue
        for ny, nx in get_next_location(y, x):
            value = adj[ny][nx] + 3 * M + dist
            if distance[ny][nx] > value:
                distance[ny][nx] = value
                heapq.heappush(q, (value, ny, nx))
        u = abs(N - 1 - y) + abs(N - 1 - x)
        if u < 3:
            value = u * M + dist
            if distance[N - 1][N - 1] > value:
                distance[N - 1][N - 1] = value
                heapq.heappush(q, (value, N - 1, N - 1))


def get_next_location(y, x):
    ret = set()
    q = deque()
    q.append((y, x, 0))
    while q:
        y, x, cnt = q.popleft()
        if cnt == 3:
            if (y, x) not in ret:
                ret.add((y, x))
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            q.append((ny, nx, cnt + 1))
    return ret


N, M = map(int, si().strip().split(" "))
adj = [list(map(int, si().strip().split(" "))) for _ in range(N)]
distance = [[INF for _ in range(N)] for _ in range(N)]
dijkstra(0, 0)
print(distance[N - 1][N - 1])
