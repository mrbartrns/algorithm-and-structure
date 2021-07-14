# BOJ 18405 (경쟁적 전염)
import heapq
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(q, board):
    while q:
        cnt, idx, y, x = heapq.heappop(q)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if board[ny][nx][1] == 0:
                board[ny][nx][0] = cnt + 1
                board[ny][nx][1] = idx
                heapq.heappush(q, (cnt + 1, idx, ny, nx))
        cnt += 1


n, k = map(int, si().split())
temp = [list(map(int, si().split())) for _ in range(n)]
graph = []
for i in range(n):
    row = []
    for j in range(n):
        row.append([0, temp[i][j]])
    graph.append(row)

arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j][1] > 0:
            heapq.heappush(arr, (0, graph[i][j][1], i, j))

bfs(arr, graph)
for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()

s, r, c = map(int, si().split())
if graph[r - 1][c - 1][0] <= s:
    print(graph[r - 1][c - 1][1])
else:
    print(0)
