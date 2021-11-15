# BOJ 3109 빵집
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline


def dfs(y, x):
    if y < 0 or y >= R:
        return 0
    if x == C:
        return 1
    if cache[y][x] > -1:
        return 0
    if adj[y][x] == "x":
        return 0
    cache[y][x] = 0
    value = dfs(y - 1, x + 1)
    if value:
        cache[y][x] = value
        return cache[y][x]
    value = dfs(y, x + 1)
    if value:
        cache[y][x] = value
        return cache[y][x]
    value = dfs(y + 1, x + 1)
    if value:
        cache[y][x] = value
        return cache[y][x]
    return cache[y][x]


R, C = map(int, si().split(" "))
adj = [list(si().strip()) for _ in range(R)]
cache = [[-1 for _ in range(C)] for _ in range(R)]

for i in range(R):
    dfs(i, 0)

answer = 0
for i in range(R):
    answer += cache[i][0]
print(answer)
