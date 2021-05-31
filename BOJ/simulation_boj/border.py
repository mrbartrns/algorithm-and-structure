# BOJ 16234
import sys
from collections import deque

si = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    que = deque()
    block = 1
    s = graph[x][y]
    que.append((x, y))
    visited[x][y] = label_number[0]
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            n2x = x + dx[i] * 2
            n2y = y + dy[i] * 2
            if nx < 0 or ny < 0 or nx >= size or ny >= size:
                continue
            if n2x < 0 or n2y < 0 or n2x >= size or n2y >= size:
                continue
            border = graph[nx][ny]
            if border == 0 and visited[n2x][n2y] == 0:
                visited[n2x][n2y] = label_number[0]
                que.append((n2x, n2y))
                block += 1
                s += graph[n2x][n2y]
    avg = s // block
    return label_number[0], avg


def open_border():
    has_opened = False
    for x in range(0, size, 2):
        for y in range(0, size, 2):
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                n2x = x + dx[k] * 2
                n2y = y + dy[k] * 2
                if nx < 0 or nx >= size or ny < 0 or ny >= size:
                    continue
                if n2x < 0 or n2x >= size or n2y < 0 or n2y >= size:
                    continue
                if L <= abs(graph[x][y] - graph[n2x][n2y]) <= R:
                    graph[nx][ny] = 0
                    has_opened = True
    return has_opened


def close_border():
    for x in range(size):
        for y in range(size):
            if not (x % 2 == 0 and y % 2 == 0):
                graph[x][y] = -1


n, L, R = map(int, si().split())
size = 2 * n
temp = [list(map(int, si().split())) for _ in range(n)]
graph = [[-1 for _ in range(102)] for _ in range(102)]

day = 0

# 겹치는 국경선을 만들지 않기 위하여 모든 배열에 * 2 씩 실행하기
for i in range(0, size, 2):
    for j in range(0, size, 2):
        graph[i][j] = temp[i // 2][j // 2]

# 그래프 출력
# for y in range(size):
#     print(" ".join(list(map(str, graph[y]))))

while open_border():
    # 국경선을 열었으면, 인접한 국가끼리 bfs 실행하기
    visited = [[0 for _ in range(102)] for _ in range(102)]
    label_number = [1]
    values = [0] * 50000
    for i in range(0, size, 2):
        for j in range(0, size , 2):
            if visited[i][j] == 0:
                label, average = bfs(i, j)
                values[label] = average
                label_number[0] += 1

    # 모든 지점에 대해 탐색이 끝났으면, 라벨링 한 값으로 그래프 값 변경하기
    for i in range(0, size, 2):
        for j in range(0, size, 2):
            label_value = visited[i][j]
            graph[i][j] = values[label_value]

    # 그래프 출력
    # for y in range(2 * n):
    #     print(" ".join(list(map(str, graph[y]))))

    # 국경 닫기
    close_border()
    # 날짜 더하기
    day += 1

print(day)
