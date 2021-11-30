# BOJ 1944 복제 로봇
"""
로봇은 복제 장치를 이용하면 자기 자신을 똑같은 로봇으로 복제할 수 있다.
미로에 이 로봇을 풀었다. -> 미로에 흩어진 열쇠들을 모두 찾아야 함
열쇠가 있는 곳들과 로봇이 출발하는 위치에 로봇이 복제할 수 있는 장치 있음
모든 열쇠를 찾으면서 로봇이 움직이는 횟수의 합이 최소가 되도록
다익스트라: 어떤 지점을 거치던 간에 시작 지점에서 특정 지점까지 최단 거리를 나타냄
복제를 어떻게 표현해야 되는지?
"""
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def memset(vector, value):
    for i in range(len(vector)):
        vector[i] = value


def graph_memset(graph, value):
    for i in range(len(graph)):
        memset(graph[i], value)


def find_keys(graph):
    keys = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == "K" or graph[i][j] == "S":
                keys.append((i, j))
    return keys


def dijkstra(sy, sx):
    q = deque()
    visited[sy][sx] = True
    q.append((sy, sx, 0))
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if graph[ny][nx] == "1":
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, cnt + 1))
                if graph[ny][nx] == "K" or graph[ny][nx] == "S":
                    n1, n2 = 0, 0
                    for i in range(M + 1):
                        ky, kx = keys[i]
                        if (sy, sx) == (ky, kx):
                            n1 = i
                        if (ny, nx) == (ky, kx):
                            n2 = i
                    edges.append((n1, n2, cnt + 1))


def find(arr, a):
    if arr[a] == a:
        return a
    arr[a] = find(arr, arr[a])
    return arr[a]


def union(arr, a, b):
    a = find(arr, a)
    b = find(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


def kruskal():
    ret = 0
    cnt = 0
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(M + 1)]
    for a, b, c in edges:
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            cnt += 1
            ret += c
            if cnt == M:
                return ret
    return INF


N, M = map(int, si().split(" "))
graph = [list(si().strip()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
keys = find_keys(graph)
edges = []
for ky, kx in keys:
    dijkstra(ky, kx)
    graph_memset(visited, False)
answer = kruskal()
print(answer if answer < INF else -1)
