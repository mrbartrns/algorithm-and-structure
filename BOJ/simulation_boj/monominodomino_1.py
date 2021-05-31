# BOJ 20061
"""
방향 이동시 while문 사용하여 빠른 속도로 구현하는것이 중요
"""

import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def move(t, y, x):
    # blue
    b_idx, g_idx = 0, 0
    if t == 1:
        while x + b_idx < 10 and graph[y][x + b_idx] == 0:
            b_idx += 1
        b_idx -= 1
        graph[y][x + b_idx] = 1
        while y + g_idx < 10 and graph[y + g_idx][x] == 0:
            g_idx += 1
        g_idx -= 1
        graph[y + g_idx][x] = 1
    elif t == 2:  # --
        while x + 1 + b_idx < 10 and graph[y][x + b_idx] == 0 and graph[y][x + b_idx + 1] == 0:
            b_idx += 1
        b_idx -= 1  # 하나 더 움직이기때문에 마지막에 빼줘야 함. 한쪾방향으로만 움직일 경우 이 방법이 이득
        graph[y][x + b_idx], graph[y][x + b_idx + 1] = 1, 1
        while y + g_idx < 10 and graph[y + g_idx][x] == 0 and graph[y + g_idx][x + 1] == 0:
            g_idx += 1
        g_idx -= 1
        graph[y + g_idx][x], graph[y + g_idx][x + 1] = 1, 1
    else:  # |
        while x + b_idx < 10 and graph[y][x + b_idx] == 0 and graph[y + 1][x + b_idx] == 0:
            b_idx += 1
        b_idx -= 1
        graph[y][x + b_idx], graph[y + 1][x + b_idx] = 1, 1
        while y + 1 + g_idx < 10 and graph[y + g_idx][x] == 0 and graph[y + g_idx + 1][x] == 0:
            g_idx += 1
        g_idx -= 1
        graph[y + g_idx][x], graph[y + g_idx + 1][x] = 1, 1


def clear():
    ans = 0
    for i in range(10):
        # remove blue line
        if graph[0][i] == graph[1][i] == graph[2][i] == graph[3][i] == 1:
            ans += 1
            for j in range(i, 0, -1):
                graph[0][j], graph[1][j], graph[2][j], graph[3][j] = graph[0][j - 1], graph[1][j - 1], \
                                                                     graph[2][j - 1], graph[3][j - 1]
            graph[0][0], graph[1][0], graph[2][0], graph[3][0] = 0, 0, 0, 0

    for i in range(10):
        if graph[i][0] == graph[i][1] == graph[i][2] == graph[i][3] == 1:
            ans += 1
            for j in range(i, 0, -1):
                graph[j][0], graph[j][1], graph[j][2], graph[j][3] = graph[j - 1][0], graph[j - 1][1], \
                                                                     graph[j - 1][2], graph[j - 1][3]
            graph[0][0], graph[0][1], graph[0][2], graph[0][3] = 0, 0, 0, 0
    return ans


def remove():
    # blue
    cnt = 0
    for i in range(2):
        if graph[0][4 + i] == 1 or graph[1][4 + i] == 1 or graph[2][4 + i] == 1 or graph[3][4 + i] == 1:
            cnt += 1
    for _ in range(cnt):
        for i in range(9, 4, -1):
            graph[0][i], graph[1][i], graph[2][i], graph[3][i] = graph[0][i - 1], graph[1][i - 1], graph[2][i - 1], \
                                                                 graph[3][i - 1]
        graph[0][4], graph[1][4], graph[2][4], graph[3][4] = 0, 0, 0, 0

    # green
    cnt = 0
    for i in range(2):
        if graph[i + 4][0] == 1 or graph[i + 4][1] == 1 or graph[i + 4][2] == 1 or graph[i + 4][3] == 1:
            cnt += 1

    for _ in range(cnt):
        for i in range(9, 4, -1):
            graph[i][0], graph[i][1], graph[i][2], graph[i][3] = graph[i - 1][0], graph[i - 1][1], graph[i - 1][2], \
                                                                 graph[i - 1][3]
        graph[4][0], graph[4][1], graph[4][2], graph[4][3] = 0, 0, 0, 0


n = int(si())
blocks = []
graph = [[0 for _ in range(10)] for _ in range(10)]
score = 0
block_cnt = 0
for _ in range(n):
    a, b, c = map(int, si().split())
    blocks.append((a, b, c))  # t, y, x

for a, b, c in blocks:
    move(a, b, c)
    score += clear()
    remove()

for i in range(10):
    for j in range(10):
        if graph[i][j] == 1:
            block_cnt += 1
    #     print(graph[i][j], end=" ")
    # print()
print(score)
print(block_cnt)
