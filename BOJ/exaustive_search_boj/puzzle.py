# BOJ 1525
import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    que = deque()
    que.append((x, y, 0, -1, -1))

    while que:
        x, y, cnt, last_x, last_y = que.popleft()
        print(matrix[x][y])
        if last_x >= 0 and last_y >= 0:
            matrix[x][y], matrix[last_x][last_y] = matrix[last_x][last_y], matrix[x][y]
            print(matrix[x][y])
        if ref == matrix:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue

            # 변하는 좌표값을 보존하기 위해서는 다른 방법이 필요하다.
            if nx != last_x and ny != last_y:
                matrix[nx][ny], matrix[x][y] = matrix[x][y], matrix[nx][ny]
                que.append((nx, ny, cnt + 1, x, y))
                matrix[nx][ny], matrix[x][y] = matrix[x][y], matrix[nx][ny]


ref = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
matrix = []
location = [()] * 9
for _ in range(3):
    matrix.append(list(map(int, si().split())))

for i in range(3):
    for j in range(3):
        location[matrix[i][j]] = (i, j)

x, y = location[0][0], location[0][1]
print(bfs(x, y))
