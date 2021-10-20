# BOJ 3055 탈출
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def get_water_point(flow):
    ret = []
    for y in range(R):
        for x in range(C):
            if flow[y][x] == 0:
                ret.append((y, x))
    return ret


def get_init_location(maps):
    for y in range(R):
        for x in range(C):
            if maps[y][x] == "S":
                return y, x


def get_water_graph(graph):
    ret = [[INF for _ in range(C)] for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if graph[y][x] == "*":
                ret[y][x] = 0
    return ret


def bfs_flow(flow, maps):
    st = get_water_point(flow)
    q = []
    for y, x in st:
        heapq.heappush(q, (0, y, x))
    while q:
        cnt, y, x = heapq.heappop(q)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            if cnt + 1 < flow[ny][nx] and maps[ny][nx] == ".":
                flow[ny][nx] = cnt + 1
                heapq.heappush(q, (cnt + 1, ny, nx))


def bfs(flow, maps):
    q = []
    y, x = get_init_location(maps)
    flow[y][x] = 0
    heapq.heappush(q, (0, y, x))
    while q:
        cnt, y, x = heapq.heappop(q)
        if maps[y][x] == "D":
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            if maps[ny][nx] == "X":
                continue
            if cnt + 1 < flow[ny][nx]:
                flow[ny][nx] = cnt + 1
                heapq.heappush(q, (cnt + 1, ny, nx))
    return "KAKTUS"


R, C = map(int, si().split(" "))
graph = [list(si().strip()) for _ in range(R)]
water_graph = get_water_graph(graph)
bfs_flow(water_graph, graph)
print(bfs(water_graph, graph))
