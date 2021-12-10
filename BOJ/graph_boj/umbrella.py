# BOj 17244 아맞다우산
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dijkstra(sy, sx):
    q = []
    distance[0][sy][sx] = 0
    heapq.heappush(q, (0, 0, sy, sx))
    while q:
        cnt, mask, y, x = heapq.heappop(q)
        if distance[mask][y][x] < cnt:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if adj[ny][nx] == "#":
                continue
            n_mask = mask
            if adj[ny][nx] == "X":
                idx = idxs[ny][nx]
                if ((1 << idx) & n_mask) == 0:
                    n_mask ^= 1 << idx
            if distance[n_mask][ny][nx] > cnt + 1:
                distance[n_mask][ny][nx] = cnt + 1
                heapq.heappush(q, (cnt + 1, n_mask, ny, nx))


M, N = map(int, si().strip().split(" "))
adj = [list(si().strip()) for _ in range(N)]
idxs = [[-1 for _ in range(M)] for _ in range(N)]
count = 0
spy, spx = 0, 0
epy, epx = 0, 0
for i in range(N):
    for j in range(M):
        if adj[i][j] == "X":
            idxs[i][j] = count
            count += 1
        elif adj[i][j] == "S":
            spy, spx = i, j
        elif adj[i][j] == "E":
            epy, epx = i, j
distance = [[[INF for _ in range(M)] for _ in range(N)] for _ in range(1 << count)]
dijkstra(spy, spx)
print(distance[(1 << count) - 1][epy][epx])
