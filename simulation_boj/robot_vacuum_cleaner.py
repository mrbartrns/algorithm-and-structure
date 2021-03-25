# BOJ 14053
import sys
from collections import deque

si = sys.stdin.readline


def solve(x, y, d):
    que = deque()
    que.append((x, y, d))
    cnt = 0
    while que:
        x, y, d = que.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            cnt += 1
        flag = 0
        direction = d
        while flag < 4:
            direction = (direction + 3) % 4
            if (
                direction == 0
                and x - 1 >= 0
                and graph[x - 1][y] == 0
                and not visited[x - 1][y]
            ):
                que.append((x - 1, y, direction))
                break
            elif (
                direction == 1
                and y + 1 < m
                and graph[x][y + 1] == 0
                and not visited[x][y + 1]
            ):
                que.append((x, y + 1, direction))
                break
            elif (
                direction == 2
                and x + 1 < n
                and graph[x + 1][y] == 0
                and not visited[x + 1][y]
            ):
                que.append((x + 1, y, direction))
                break
            elif (
                direction == 3
                and y - 1 >= 0
                and graph[x][y - 1] == 0
                and not visited[x][y - 1]
            ):
                que.append((x, y - 1, direction))
                break
            elif flag < 4:
                flag += 1

        if flag == 4:
            if direction == 0 and x + 1 < n and graph[x + 1][y] == 0:
                que.append((x + 1, y, direction))
            elif direction == 1 and y - 1 >= 0 and graph[x][y - 1] == 0:
                que.append((x, y - 1, direction))
            elif direction == 2 and x - 1 >= 0 and graph[x - 1][y] == 0:
                que.append((x - 1, y, direction))
            elif direction == 3 and y + 1 < m and graph[x][y + 1] == 0:
                que.append((x, y + 1, direction))

    return cnt


"""
n, m = map(int, si().split())
x, y, d = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
"""

n, m = 11, 10
graph = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
x, y, d = 7, 4, 0
"""
n, m = 5, 5
graph = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
x, y, d = 2, 2, 0
"""
visited = [[False for _ in range(m)] for _ in range(n)]
print(solve(x, y, d))