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
            visited[y][x] = True
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                

print(graph)
