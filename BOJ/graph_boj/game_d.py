# BOJ 1584 게임
import heapq
import sys

# constants
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# functions
def dijkstra(sy, sx):
    q = []
    visited[sy][sx] = 0
    heapq.heappush(q, (0, sy, sx))
    while q:
        cnt, y, x = heapq.heappop(q)
        # print(cnt, y, x)
        if visited[y][x] < cnt:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 501 or nx < 0 or nx >= 501:
                continue
            if board[ny][nx] == 2:
                continue
            value = cnt
            if board[ny][nx] == 1:
                value += 1
            if visited[ny][nx] > value:
                visited[ny][nx] = value
                heapq.heappush(q, (value, ny, nx))
    return visited[500][500]


# initialize
board = [[0 for _ in range(501)] for _ in range(501)]
visited = [[INF for _ in range(501)] for _ in range(501)]
A = int(si())
for _ in range(A):
    y1, x1, y2, x2 = map(int, si().split(" "))
    if y1 > y2:
        y1, y2 = y2, y1
    if x1 > x2:
        x1, x2 = x2, x1
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            board[i][j] = 1
B = int(si())
for _ in range(B):
    y1, x1, y2, x2 = map(int, si().split(" "))
    if y1 > y2:
        y1, y2 = y2, y1
    if x1 > x2:
        x1, x2 = x2, x1
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            board[i][j] = 2
result = dijkstra(0, 0)
print(result if result < INF else -1)
