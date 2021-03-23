# BOJ 14500
# 풀이 보기
import sys

si = sys.stdin.readline

s = 0
n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        # case 1 - 1
        if j - 3 >= 0:
            s = max(
                s, graph[i][j - 3] + graph[i][j - 2] + graph[i][j - 1] + graph[i][j]
            )
        # case 1 - 2
        if i - 3 >= 0:
            s = max(
                s, graph[i - 3][j] + graph[i - 2][j] + graph[i - 1][j] + graph[i][j]
            )
        # case 2 - 1:
        if i - 1 >= 0 and j - 1 >= 0:
            s = max(
                s, graph[i - 1][j - 1] + graph[i - 1][j] + graph[i][j - 1] + graph[i][j]
            )
        # case 3 - 1:
        if i - 1 >= 0 and j - 2 >= 0:
            s = max(
                s,
                graph[i][j - 2]
                + graph[i - 1][j - 2]
                + graph[i - 1][j - 1]
                + graph[i - 1][j],
            )
        # case 3 - 3:
        if i - 2 >= 0 and j - 1 >= 0:
            s = max(
                s,
                graph[i - 2][j - 1]
                + graph[i - 1][j - 1]
                + graph[i][j - 1]
                + graph[i][j],
            )
        # case 3 - 3:
        if i - 1 >= 0 and j - 2 >= 0:
            s = max(
                s, graph[i][j - 2] + graph[i][j - 1] + graph[i][j] + graph[i - 1][j]
            )
        # case 3 - 4:
        if i - 2 >= 0 and j - 1 >= 0:
            s = max(
                s, graph[i - 2][j - 1] + graph[i - 2][j] + graph[i - 1][j] + graph[i][j]
            )
        # case 4 - 1:
        if i - 1 >= 0 and j - 2 >= 0:
            s = max(
                s,
                graph[i][j - 1]
                + graph[i - 1][j - 2]
                + graph[i - 1][j - 1]
                + graph[i - 1][j],
            )
        # case 4 - 2:
        if i - 2 >= 0 and j - 1 >= 0:
            s = max(
                s, graph[i - 1][j - 1] + graph[i - 2][j] + graph[i - 1][j] + graph[i][j]
            )
        # case 4 - 3:
        if i - 1 >= 0 and j - 2 >= 0:
            s = max(
                s, graph[i - 1][j - 1] + graph[i][j - 2] + graph[i][j - 1] + graph[i][j]
            )
        # case 4 - 4:
        if i - 2 >= 0 and j - 1 >= 0:
            s = max(
                s,
                graph[i - 2][j - 1]
                + graph[i - 1][j - 1]
                + graph[i][j - 1]
                + graph[i - 1][j],
            )
        # case 5 - 1:
        if i - 1 >= 0 and j - 2 >= 0:
            s = max(
                s,
                graph[i - 1][j]
                + graph[i - 1][j - 1]
                + graph[i][j - 1]
                + graph[i][j - 2],
            )
        # case 5 - 2:
        if i - 2 >= 0 and j - 1 >= 0:
            s = max(
                s,
                graph[i - 2][j - 1]
                + graph[i - 1][j - 1]
                + graph[i - 1][j]
                + graph[i][j],
            )
print(s)