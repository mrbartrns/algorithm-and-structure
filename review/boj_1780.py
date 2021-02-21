# BOJ 1780
import sys

si = sys.stdin.readline

n = int(si())
graph = []
for _ in range(n):
    graph.append(list(map(int, si().split())))

"""
n = 9
graph = [
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, -1, 0, 1, -1, 0, 1, -1],
    [0, -1, 1, 0, 1, -1, 0, 1, -1],
    [0, 1, -1, 1, 0, -1, 0, 1, -1],
]
"""

counts = [0, 0, 0]


def divide(x, y, k):

    if k == 1:
        val = graph[x][y]
        counts[val + 1] += 1
        return

    flag = True
    val = graph[x][y]
    for i in range(x, x + k):
        for j in range(y, y + k):
            if val != graph[i][j]:
                flag = False
                break

    if flag:
        counts[val + 1] += 1
    else:
        for i in range(3):
            for j in range(3):
                divide(x + (k // 3) * i, y + (k // 3) * j, k // 3)


divide(0, 0, n)
print("\n".join(map(str, counts)))