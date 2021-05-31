# BOJ 15686
import sys
from itertools import combinations

si = sys.stdin.readline

n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
chickens = []
remains = []
MIN = 1e12

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickens.append((i, j))

for i in range(m):
    remains.extend(list(combinations(chickens, i + 1)))


for remain in remains:
    preset = set(remain)
    s = 0
    for i in range(n):
        for j in range(n):
            temp = 100000000
            if graph[i][j] == 1:
                for x, y in preset:
                    temp = min(abs(x - i) + abs(y - j), temp)
                s += temp
    if MIN > s:
        MIN = s

print(MIN)