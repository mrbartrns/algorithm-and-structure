# BOj 3085
import sys

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(si())
graph = [list(si().strip()) for _ in range(n)]
max_cnt = 1


def solve(x, y):
    # 중간에 끊어진것에 대한 카운트를 하면 안됨
    max_counts = 0
    counts = 0
    char = ""
    for i in range(n):
        if not char or char != graph[x][i]:
            char = graph[x][i]
            max_counts = max(counts, max_counts)
            counts = 1
        else:
            counts += 1
    max_counts = max(counts, max_counts)
    char = ""
    counts = 0
    for i in range(n):
        if not char or char != graph[i][y]:
            char = graph[i][y]
            max_counts = max(counts, max_counts)
            counts += 1
        else:
            counts += 1
    max_counts = max(counts, max_counts)
    return max_counts


for x in range(n):
    for y in range(n):
        for i in range(4):
            cnt = 0
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
            cnt = solve(x, y)
            max_cnt = max(max_cnt, cnt)
            graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]

print(max_cnt)
