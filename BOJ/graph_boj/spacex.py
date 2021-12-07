import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def dijkstra(start):
    q = []
    distance[start][1 << start] = 0
    heapq.heappush(q, (0, start, 1 << start))
    while q:
        dist, cur, mask = heapq.heappop(q)
        if distance[cur][mask] < dist:
            continue
        for nxt in range(N):
            n_mask = mask | 1 << nxt
            if distance[nxt][n_mask] > dist + adj[cur][nxt]:
                distance[nxt][n_mask] = dist + adj[cur][nxt]
                heapq.heappush(q, (dist + adj[cur][nxt], nxt, n_mask))


N, M = map(int, si().strip().split(" "))
distance = [[INF for _ in range(2 ** N)] for _ in range(N)]
adj = [list(map(int, si().strip().split(" "))) for _ in range(N)]
dijkstra(M)
answer = INF
for i in range(N):
    answer = min(distance[i][(1 << N) - 1], answer)
print(answer)
