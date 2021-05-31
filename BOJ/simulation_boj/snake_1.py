# BOJ 3190
import sys
from collections import deque

si = sys.stdin.readline

# 북 동 남 서 # direction회전을 이용할때는 이렇게 표기하는게 더 직관적으로 사용 가능
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def play(graph, orders):
    direction = 1  # 0: 북 1: 동 2: 남 3: 서
    time = 1
    que = deque()  # 뱀의 총 길이
    x, y = 0, 0  # 뱀의 head 정보
    que.append((x, y))
    graph[x][y] = 1  # 뱀의 정보를 입력했더라도 그래프에 표시해야함
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            return time

        if graph[nx][ny] == 1:
            return time

        que.append((nx, ny))
        if graph[nx][ny] == 0:
            ox, oy = que.popleft()
            graph[ox][oy] = 0
        graph[nx][ny] = 1
        x, y = nx, ny

        # 이 아래 방향 바꾸는 정보가 들어감
        if orders[time] == "D":  # 오른쪽으로 회전
            direction = (direction + 1) % 4
        elif orders[time] == "L":
            direction = (direction + 3) % 4
        time += 1


n = int(si())
apple = int(si())
orders = [""] * 10001

graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(apple):
    i, j = map(int, si().split())
    graph[i - 1][j - 1] = 2  # 2는 사과

order_count = int(si())
for _ in range(order_count):
    a, b = si().split()
    orders[int(a)] = b

print(play(graph, orders))