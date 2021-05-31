# BOJ 1261
import sys
import heapq

si = sys.stdin.readline

INF = 1e9

"""
빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.
1, 1의 운영진이 n, m으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램
0 -> 자유롭게 이동할 수 있는 방
1 -> 벽을 부셔야 하는 방 => 0으로 만들기
n, m에 도달하면, 더이상 탐색하지 않기
visited 배열을 만들어 이미 탐색한 지역은 더 이상 탐색하지 않기?
-> 이럴 경우 최소값을 찾을 수 없음. 모든 경우에 대해서 탐색을 해야함
"""
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, si().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, si().strip())))

distance = [[INF for _ in range(m)] for _ in range(n)]


def dijkstra(x, y):
    q = []
    distance[x][y] = 0
    heapq.heappush(q, (0, x, y))
    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    return distance[n - 1][m - 1]


print(dijkstra(0, 0))