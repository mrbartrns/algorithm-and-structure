# BOJ 과외맨
from collections import deque
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321
dy_odd = [-1, -1, 0, 0, 1, 1]
dy_even = [-1, -1, 0, 0, 1, 1]
dx_odd = [0, 1, -1, 1, 0, 1]
dx_even = [0, -1, 1, -1, 0, -1]
compare_odd = [0, 1, 0, 1, 0, 1]  # compare_next = 1 - compare_cur[i]
compare_even = [1, 0, 1, 0, 1, 0]


def dijkstra(start):
    q = []
    ret = 0
    distance[start] = 1
    heapq.heappush(q, (1, 0, 0))  # dist, y, x
    while q:
        dist, y, x = heapq.heappop(q)
        cur = adj[y][x]
        if distance[cur] < dist:
            continue
        for i in range(6):
            ny = 0
            nx = 0
            if y % 2 == 0:
                ny = y + dy_even[i]
                nx = x + dx_even[i]
            else:
                ny = y + dy_odd[i]
                nx = x + dx_odd[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if adj[ny][nx] == -1:
                continue
            nxt = adj[ny][nx]
            compare_cur = 0
            compare_next = 0
            if y % 2 == 0:
                compare_cur = info[cur][compare_even[i]]
                compare_next = info[nxt][1 - compare_even[i]]
            else:
                compare_cur = info[cur][compare_odd[i]]
                compare_next = info[nxt][1 - compare_odd[i]]
            if compare_cur != compare_next:
                continue
            if distance[nxt] > dist + 1:
                distance[nxt] = dist + 1
                ret = max(ret, nxt)
                heapq.heappush(q, (dist + 1, ny, nx))
                prev[nxt] = cur
    return ret


N = int(si())
node_count = N * N - N // 2

adj = [[-1 for _ in range(N)] for _ in range(N)]
distance = [INF] * node_count
info = []
prev = [-1] * node_count
visited = [False] * node_count
cnt = 0
for _ in range(node_count):
    a, b = map(int, si().split(" "))
    info.append((a, b))
for i in range(N):
    for j in range(N):
        if i % 2 == 1 and j == N - 1:
            continue
        adj[i][j] = cnt
        cnt += 1
max_node = dijkstra(0)
print(distance[max_node])
n = max_node
ret = deque()
while n != -1:
    ret.appendleft(n + 1)
    n = prev[n]
while ret:
    print(ret.popleft(), end=" ")
