# BOJ 2917 늑대 사냥꾼
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def dijkstra():
    q = []
    for ty, tx in trees:
        distance[ty][tx] = 0
        heapq.heappush(q, (0, ty, tx))
    while q:
        cnt, y, x = heapq.heappop(q)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if distance[ny][nx] > 1 + cnt:
                distance[ny][nx] = 1 + cnt
                heapq.heappush(q, (1 + cnt, ny, nx))


def bfs(sy, sx, ey, ex):
    q = []
    answer = INF
    visited = [[False for _ in range(M)] for _ in range(N)]
    heapq.heappush(q, (-distance[sy][sx], sy, sx))
    while q:
        cost, y, x = heapq.heappop(q)
        answer = min(answer, -cost)
        if y == ey and x == ex:
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                heapq.heappush(q, (-distance[ny][nx], ny, nx))
    return answer


N, M = map(int, si().strip().split(" "))
graph = [list(si().strip()) for _ in range(N)]
distance = [[INF for _ in range(M)] for _ in range(N)]
trees = []
start_y, start_x = 0, 0
end_y, end_x = 0, 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "V":
            start_y, start_x = i, j
        elif graph[i][j] == "J":
            end_y, end_x = i, j
        elif graph[i][j] == "+":
            trees.append((i, j))
dijkstra()
print(bfs(start_y, start_x, end_y, end_x))
