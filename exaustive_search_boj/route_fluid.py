# BOJ 11403
import sys

si = sys.stdin.readline

n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(n):
    print(" ".join(list(map(str, graph[i]))))
