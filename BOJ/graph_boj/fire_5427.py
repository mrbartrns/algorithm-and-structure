# BOJ 5427 불
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def get_fire_location(maps):
    ret = []
    for y in range(M):
        for x in range(N):
            if maps[y][x] == "*":
                ret.append((y, x))
    return ret


def get_location(maps):
    for y in range(M):
        for x in range(N):
            if maps[y][x] == "@":
                return y, x


def dijkstra_fire(distance, maps, location):
    q = []
    for y, x in location:
        distance[y][x] = 0
        heapq.heappush(q, (0, y, x))
    while q:
        cost, y, x = heapq.heappop(q)
        if distance[y][x] < cost:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= M or nx < 0 or nx >= N:
                continue
            if maps[ny][nx] == "#":
                continue
            if cost + 1 < distance[ny][nx]:
                heapq.heappush(q, (cost + 1, ny, nx))
                distance[ny][nx] = cost + 1


def dijkstra(distance, maps, sy, sx):
    q = []
    distance[sy][sx] = 0
    heapq.heappush(q, (0, sy, sx))
    while q:
        cost, y, x = heapq.heappop(q)
        if distance[y][x] < cost:
            continue
        if y == 0 or y == M - 1 or x == 0 or x == N - 1:
            return cost + 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= M or nx < 0 or nx >= N:
                continue
            if maps[ny][nx] == "#":
                continue
            if cost + 1 < distance[ny][nx]:
                heapq.heappush(q, (cost + 1, ny, nx))
                distance[ny][nx] = cost + 1
    return INF


T = int(si())
for _ in range(T):
    N, M = map(int, si().split(" "))
    graph = [list(si().strip()) for _ in range(M)]
    visited = [[INF for _ in range(N)] for _ in range(M)]
    fire_location = get_fire_location(graph)
    py, px = get_location(graph)
    dijkstra_fire(visited, graph, fire_location)
    answer = dijkstra(visited, graph, py, px)
    print(answer if answer < INF else "IMPOSSIBLE")
