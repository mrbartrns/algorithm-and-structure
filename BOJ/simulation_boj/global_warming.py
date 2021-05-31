# BOJ 5212
import sys

si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def change(el):
    if el == ".":
        el = 0
    elif el == "X":
        el = 1
    return el


n, m = map(int, si().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    temp = list(si().strip())
    ap = list(map(change, temp))
    graph.append(ap)

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            cnt = 0
            visited[y][x] = True
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    cnt += 1
                    continue
                elif graph[ny][nx] == 0:
                    cnt += 1
            if cnt >= 3:
                visited[y][x] = False


start_r, start_c = n, m
end_r, end_c = 0, 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            start_r = min(start_r, i)
            start_c = min(start_c, j)
            end_r = max(end_r, i)
            end_c = max(end_c, j)

for i in range(start_r, end_r + 1):
    for j in range(start_c, end_c + 1):
        print("." if not visited[i][j] else "X", end="")
    print()


