# BOJ 1194 달이 차오른다, 가자.
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dijkstra(sy: int, sx: int) -> None:
    q = []
    distance[0][sy][sx] = 0
    heapq.heappush(q, (0, 0, sy, sx))  # dist, mask, y, x
    while q:
        dist, mask, y, x = heapq.heappop(q)
        if distance[mask][y][x] < dist:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            n_mask = mask
            # filter that ny nx in out of range
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            # filter that adj[ny][nx] is #
            if adj[ny][nx] == "#":
                continue
            # if adj[ny][nx] is the lock
            if ord("A") <= ord(adj[ny][nx]) <= ord("F"):
                if n_mask & (1 << ord(adj[ny][nx]) - ord("A")) == 0:
                    continue
            # if adj[ny][nx] is the key
            if ord("a") <= ord(adj[ny][nx]) <= ord("f"):
                n_mask = mask | (1 << (ord(adj[ny][nx]) - ord("a")))
            if distance[n_mask][ny][nx] > dist + 1:
                distance[n_mask][ny][nx] = dist + 1
                heapq.heappush(q, (dist + 1, n_mask, ny, nx))


N, M = map(int, si().strip().split(" "))
adj = [list(si().strip()) for _ in range(N)]
# N, M = 1, 7
# adj = [["f", "0", ".", "F", ".", ".", "1"]]
distance = [[[INF for _ in range(M)] for _ in range(N)] for _ in range(1 << 6)]

start_y, start_x = 0, 0
for i in range(N):
    for j in range(M):
        if adj[i][j] == "0":
            start_y, start_x = i, j
dijkstra(start_y, start_x)
answer = INF
for i in range(N):
    for j in range(M):
        if adj[i][j] == "1":
            for k in range(1 << 6):
                answer = min(answer, distance[k][i][j])
print(answer if answer < INF else -1)
