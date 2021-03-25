# BOJ 18111
import sys

si = sys.stdin.readline

n, m, b = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
MIN = 256
MAX = -1
res = 1e12
h = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] < MIN:
            MIN = graph[i][j]
        if graph[i][j] > MAX:
            MAX = graph[i][j]

for i in range(MIN, MAX + 1):
    block = b
    time = 0
    for x in range(n):
        for y in range(m):
            height = graph[x][y] - i
            if height < 0:
                block += height
                time -= height
            elif height > 0:
                block += height
                time += height * 2
    if block >= 0:
        if res >= time:
            res = time
            h = i

print(res, h)