# BOJ 1525
import sys
from collections import deque

si = sys.stdin.readline
ref = 123456789

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = 0
matrix = []
visited = {}
for _ in range(3):
    matrix.append(list(map(int, si().split())))

for i in range(3):
    for j in range(3):
        if matrix[i][j] == 0:
            matrix[i][j] = 9
        n = n * 10 + matrix[i][j]


def bfs(v):
    que = deque([v])
    visited[v] = 0
    while que:
        v = que.popleft()
        if v == ref:
            return visited[v]

        str_v = str(v)
        z = str_v.find("9")
        x = z // 3
        y = z % 3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue

            temp = list(str_v)
            temp[nx * 3 + ny], temp[z] = temp[z], temp[nx * 3 + ny]
            n_n = int("".join(temp))
            if not visited.get(n_n):
                visited[n_n] = visited[v] + 1
                que.append(n_n)
    return -1


sys.stdout.write(str(bfs(n)))