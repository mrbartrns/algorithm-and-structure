"""
미로탐색 등의 유형은 너비 우선 탐색으로 해야 시간 초과가 나지 않음
"""
# 백준 2178 - 미로탐색

from collections import deque
import sys


def bfs(v_maze):
    queue = deque([])  # to_visit
    queue.append([0, 0])
    v_maze[0][0] = 1

    while queue:
        t = queue.popleft()
        x, y = t[0], t[1]
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < len(maze) and ny < len(maze[0]):
                if maze[nx][ny] == 1 and v_maze[nx][ny] == 0:
                    queue.append([nx, ny])
                    v_maze[nx][ny] += v_maze[x][y] + 1

    return v_maze[-1][-1]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().split())
maze = []
# maze = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
for _ in range(n):
    string = sys.stdin.readline()
    column = [int(x) for x in string if x != "\n"]
    maze.append(column)
v_maze = [[0 for _ in range(m)] for _ in range(n)]
print(bfs(v_maze))
