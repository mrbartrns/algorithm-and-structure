# BOJ 17837
"""
체스판과 말을 이용하여 새로운 게임 만들기 (크기가 N * N인 체스판, 사용하는 말의 갯수는 K개)
말은 원판 모양이고, 하나의 말 위에 다른 말을 올릴 수 있음
체스판은 흰, 빨, 파 중 하나로 색칠 되어 있음
게임은 체스판위에 K개의 말을 올려놓고 시작 (1번부터 K번까지 번호와 이동방향이 정해져 있음)
말의 이동 방향에 있는 칸에 따라서 이동이 다르며 턴이 진행되던중 말이 한칸에 4개 이상 쌓이는 순간 게임이 종료
A번 말이 이동하려는 칸이
1. 흰색일 경우 그 칸으로 이동 (이동하려는 칸에 이미 말이 있는 경우, 가장 위에 A번 말을 올려놓기)
- A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 같이 이동
- A, B, C로 쌓여있고 이동하려는 칸에 D, E가 있는경우 (D, E, A, B, C)가 된다
2. 빨간색일 경우 이동한 후 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 바꾼다.
- A, D, F, G가 이동하고 이동하는 칸에 E, C, B가 있을 경우 (E, C, B, G, F, D, A)가 됨
3. 파란색의 경우, A번 말의 이동방향을 반대로 하고, 한칸 이동
- 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색일 경우 이동하지 않고 가만히 있기
- 체스판을 벗어나는 경우는 파란색과 같은 경우
"""
import sys
from collections import deque

si = sys.stdin.readline
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

N, K = map(int, si().split())
chess = [list(map(int, si().split())) for _ in range(N)]
graph = [[[] for _ in range(N)] for _ in range(N)]
horses = []
for i in range(K):
    a, b, c = map(int, si().split())
    graph[a - 1][b - 1].append(i)
    horses.append([a - 1, b - 1, c - 1])


# N, K = 4, 4
# chess = [[0, 0, 2, 0],
#          [0, 0, 1, 0],
#          [0, 0, 1, 2],
#          [0, 2, 0, 0]]
# graph = [[[], [], [], []],
#          [[0], [2], [], []],
#          [[], [1], [], []],
#          [[3], [], [], []]]
# horses = [[1, 0, 0], [2, 1, 2], [1, 1, 0], [3, 0, 1]]


def pop_elements(cur_idx):
    y, x, direction = horses[cur_idx]
    temp = deque()
    while graph[y][x] and graph[y][x][-1] != cur_idx:
        c = graph[y][x].pop()
        temp.appendleft(c)
    c = graph[y][x].pop()
    temp.appendleft(c)

    ny = y + dy[direction]
    nx = x + dx[direction]
    if ny < 0 or ny >= N or nx < 0 or nx >= N or chess[ny][nx] == 2:
        if direction == 0:
            direction = 1
        elif direction == 1:
            direction = 0
        elif direction == 2:
            direction = 3
        else:
            direction = 2
        horses[cur_idx][2] = direction
        ny = y + dy[direction]
        nx = x + dx[direction]
    move(ny, nx, temp)  # 움직이지 않을때 문제가 생길수도 있음
    return ny, nx


def move(ny, nx, que):
    if not (ny < 0 or ny >= N or nx < 0 or nx >= N):
        if chess[ny][nx] == 0:
            graph[ny][nx] += que
            for i in range(len(que)):
                horses[que[i]][0] = ny
                horses[que[i]][1] = nx
        elif chess[ny][nx] == 1:
            for i in range(len(que)):
                horses[que[i]][0] = ny
                horses[que[i]][1] = nx
            while que:
                c = que.pop()
                graph[ny][nx].append(c)
        else:
            y, x, _ = horses[que[0]]
            graph[y][x] += que
    else:
        y, x, _ = horses[que[0]]
        graph[y][x] += que


def check():
    for y in range(N):
        for x in range(N):
            if len(graph[y][x]) >= 4:
                return True
    return False


def get_check(y, x):
    if 0 <= y < N and 0 <= x < N and len(graph[y][x]) >= 4:
        return True
    return False


time = 0

while True:
    flag = False
    if time > 1000:
        break
    time += 1
    for i in range(K):
        next_y, next_x = pop_elements(i)
        if get_check(next_y, next_x):
            flag = True
            break
    if flag:
        print(time)
        break

if not flag:
    print(-1)
