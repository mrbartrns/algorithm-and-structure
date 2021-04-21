# BOJ 1799
import sys

si = sys.stdin.readline


def backtrack(idx):
    if idx == len(s_point):
        return
    for y, x in s_point:
        if iss1[y + x] or iss2[y - x + n - 1]:
            continue
        iss1[y + x], iss2[y - x + n - 1] = True, True
        max_value[0] = max(max_value[0], idx + 1)
        backtrack(idx + 1)
        iss1[y + x], iss2[y - x + n - 1] = False, False


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
# n = 5
# graph = [
#     [1, 1, 0, 1, 1],
#     [0, 1, 0, 0, 0],
#     [1, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0],
#     [1, 0, 1, 1, 1],
# ]
s_point = []
iss1 = [False] * (2 * n)
iss2 = [False] * (2 * n)
max_value = [0]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            s_point.append((i, j))
backtrack(0)
print(max_value[0])
