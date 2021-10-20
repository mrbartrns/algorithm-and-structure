# BOJ 4179 불!
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def dijkstra_fire(maps):
    q = []
    for i in range(R):
        for j in range(C):
            if maps[i][j] == "F":
                heapq.heappush(q, (0, i, j))
                visited[i][j] = 0
    while q:
        cnt, y, x = heapq.heappop(q)

        if visited[y][x] < cnt:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            if maps[ny][nx] == "#":
                continue
            if cnt + 1 < visited[ny][nx]:
                visited[ny][nx] = cnt + 1
                heapq.heappush(q, (cnt + 1, ny, nx))


def dijkstra(maps):
    q = []
    for i in range(R):
        for j in range(C):
            if maps[i][j] == "J":
                heapq.heappush(q, (0, i, j))
                visited[i][j] = 0
    while q:
        cnt, y, x = heapq.heappop(q)

        if y < 0 or y >= R or x < 0 or x >= C:
            return cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                heapq.heappush(q, (cnt + 1, ny, nx))
                continue
            if maps[ny][nx] == "#":
                continue
            if cnt + 1 < visited[ny][nx]:
                visited[ny][nx] = cnt + 1
                heapq.heappush(q, (cnt + 1, ny, nx))
    return INF


R, C = map(int, si().split(" "))
graph = [list(si().strip()) for _ in range(R)]
visited = [[INF for _ in range(C)] for _ in range(R)]
dijkstra_fire(graph)
answer = dijkstra(graph)
print(answer if answer < INF else "IMPOSSIBLE")
