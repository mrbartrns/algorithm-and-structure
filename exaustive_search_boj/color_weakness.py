# BOJ 10026
import sys

si = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# dfs for normal
def dfs(x, y, c):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if not visited[x][y] and graph[x][y] == c:
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, c)
        return True

    return False


# dfs for weakness
def dfs_weak(x, y, c):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if (c == "R" or c == "G") and graph[x][y] == "B":
        return False

    if c == "B" and graph[x][y] != "B":
        return False

    if not visited[x][y]:
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs_weak(nx, ny, c)
        return True
    return False


n = int(si())
graph = [list(si().strip()) for _ in range(n)]
# n = 5
# graph = [
#     ["R", "R", "R", "B", "B"],
#     ["G", "G", "B", "B", "B"],
#     ["B", "B", "B", "R", "R"],
#     ["B", "B", "R", "R", "R"],
#     ["R", "R", "R", "R", "R"],
# ]
cnt1 = cnt2 = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dfs(i, j, graph[i][j]):
            cnt1 += 1
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dfs_weak(i, j, graph[i][j]):
            cnt2 += 1

print(cnt1)
print(cnt2)
