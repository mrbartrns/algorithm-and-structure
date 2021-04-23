# BOJ 2174
import sys

# sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline
dir_dic = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def move(robot, op, itr):
    y, x, d = robots[robot]
    cnt = 0
    while cnt < itr:
        if op == "L":
            d = (d + 3) % 4
        elif op == "R":
            d = (d + 1) % 4
        else:
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or ny >= a or nx < 0 or nx >= b:
                return 1, robot
            if graph[ny][nx] > 0:
                return 2, graph[ny][nx]
            graph[y][x] = 0
            graph[ny][nx] = robot
            y, x = ny, nx
        robots[robot] = [y, x, d]
        cnt += 1
    return 0, robot


a, b = map(int, si().split())  # a는 행, b는 열
graph = [[0 for _ in range(b)] for _ in range(a)]
n, m = map(int, si().split())
robots = [[-1, -1, -1]] * (n + 1)
orders = []
for i in range(1, n + 1):
    r, c, D = si().split()
    graph[int(r) - 1][int(c) - 1] = i
    robots[i] = [int(r) - 1, int(c) - 1, (dir_dic[D] + 1) % 4]

for _ in range(m):
    robot, op, itr = si().split()
    orders.append((int(robot), op, int(itr)))

flag = True
for r, o, i in orders:
    ret, rob = move(r, o, i)
    if ret == 1:
        flag = False
        print('Robot', str(r), 'crashes into the wall')
        break
    elif ret == 2:
        flag = False
        print('Robot', str(r), 'crashes into robot', str(rob))
        break

if flag:
    print('OK')
