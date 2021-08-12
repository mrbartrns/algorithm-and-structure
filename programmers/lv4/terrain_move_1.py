# 지형 이동
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(land, height):
    que = deque()
    answer = []
    visited = ['0'] * (len(land) ** 2)
    visited[0] = '1'
    que.append((0, 0, ''.join(visited), 0))
    while que:
        y, x, visited, value = que.popleft()

        if visited.count('1') == len(land) ** 2:
            answer.append(value)
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            npos = ny * len(land) + nx

            if ny < 0 or ny >= len(land) or nx < 0 or nx >= len(land):
                continue

            nvisited = list(visited)
            if visited[npos] == '0':
                nvisited[npos] = '1'
                if abs(land[ny][nx] - land[y][x]) <= height:
                    que.append((ny, nx, ''.join(nvisited), value))
                else:
                    que.append((ny, nx, ''.join(nvisited), value + abs(land[ny][nx] - land[y][x])))
    print(answer)


if __name__ == '__main__':
    land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
    height = 3
    print(solution(land, height))
