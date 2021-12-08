# BOJ 16237 견우와 직녀
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
INF = 987654321


def dijkstra(sy, sx):
    q = []
    distance[sy][sx][sy][sx] = 0
    heapq.heappush(q, (0, sy, sx, sy, sx))
    while q:
        dist, y, x, u, v = heapq.heappop(q)  # cur_distance, location(y, x), cliff(y, x)
        if distance[y][x][u][v] < dist:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            # 절벽이 겹치는 경우
            if adj[ny][nx] == -1:
                continue
            # 연속으로 절벽을 건너는 경우
            if adj[y][x] != 1 and adj[ny][nx] != 1:
                continue
            # 이미 절벽을 선택한 경우
            if adj[ny][nx] == 0 and (u > 0 or v > 0):
                continue
            # 이미 놓아져 있는 오작교를 건너는 경우
            if adj[ny][nx] > 1:
                n_dist = ((dist // adj[ny][nx]) + 1) * adj[ny][nx]
                if distance[ny][nx][u][v] > n_dist:
                    distance[ny][nx][u][v] = n_dist
                    heapq.heappush(q, (n_dist, ny, nx, u, v))
            # 절벽 선택
            elif u == 0 and v == 0 and adj[ny][nx] == 0:
                n_dist = ((dist // M) + 1) * M
                if distance[ny][nx][ny][nx] > n_dist:
                    distance[ny][nx][ny][nx] = n_dist
                    heapq.heappush(q, (n_dist, ny, nx, ny, nx))
            else:
                if distance[ny][nx][u][v] > dist + 1:
                    distance[ny][nx][u][v] = dist + 1
                    heapq.heappush(q, (dist + 1, ny, nx, u, v))


def check_crossed_cliff():
    ret = []
    for y in range(N):
        for x in range(N):
            if adj[y][x] != 0:
                continue
            check = [False, False]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue
                if adj[ny][nx] != 0:
                    continue
                check[i % 2] = True
            if check[0] and check[1]:
                ret.append((y, x))
    return ret


def display_crossed_cliff():
    cliffs = check_crossed_cliff()
    for y, x in cliffs:
        adj[y][x] = -1


N, M = map(int, si().strip().split(" "))
adj = [list(map(int, si().strip().split(" "))) for _ in range(N)]
distance = [
    [[[INF for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)
]
display_crossed_cliff()
dijkstra(0, 0)
answer = INF
for i in range(N):
    for j in range(N):
        answer = min(answer, distance[N - 1][N - 1][i][j])
print(answer)
