# BOJ 20061 모노미노도미노
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

graph = [[0 for _ in range(10)] for _ in range(10)]


def move(t, y, x):
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
    elif t == 2:
        while x + b_idx + 1 < 10 and graph[y][x + b_idx] == 0 and graph[y][x + b_idx + 1] == 0:
            b_idx += 1
        b_idx -= 1
        graph[y][x + b_idx], graph[y][x + b_idx + 1] = 1, 1
        while y + g_idx < 10 and graph[y + g_idx][x] == 0 and graph[y + g_idx][x + 1] == 0:
            g_idx += 1
        g_idx -= 1
        graph[y + g_idx][x], graph[y + g_idx][x + 1] = 1, 1
    else:
        while x + b_idx < 10 and graph[y][x + b_idx] == 0 and graph[y + 1][x + b_idx] == 0:
            b_idx += 1
        b_idx -= 1
        graph[y][x + b_idx], graph[y + 1][x + b_idx] = 1, 1

        while y + g_idx + 1 < 10 and graph[y + g_idx][x] == 0 and graph[y + g_idx + 1][x] == 0:
            g_idx += 1
        g_idx -= 1
        graph[y + g_idx][x], graph[y + g_idx + 1][x] = 1, 1


def clear():
    ans = 0
    for i in range(10):
        if graph[0][i] == graph[1][i] == graph[2][i] == graph[3][i] == 1:
            graph[0][i], graph[1][i], graph[2][i], graph[3][i] = 0, 0, 0, 0
            ans += 1
            for k in range(i, 0, -1):
                graph[0][k], graph[1][k], graph[2][k], graph[3][k] = graph[0][k - 1], graph[1][k - 1], graph[2][k - 1], \
                                                                     graph[3][k - 1]

    for i in range(10):
        if graph[i][0] == graph[i][1] == graph[i][2] == graph[i][3] == 1:
            graph[i][0], graph[i][1], graph[i][2], graph[i][3] = 0, 0, 0, 0
            ans += 1
            for k in range(i, 0, -1):
                graph[k][0], graph[k][1], graph[k][2], graph[k][3] = graph[k - 1][0], graph[k - 1][1], graph[k - 1][2], \
                                                                     graph[k - 1][3]
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
order = []
res = 0
cnt = 0
for _ in range(n):
    a, b, c = map(int, si().split())
    order.append((a, b, c))  # t, x, y

for t, r, c in order:
    move(t, r, c)
    res += clear()
    remove()

for i in range(10):
    for j in range(10):
        if graph[i][j] > 0:
            cnt += 1

print(res)
print(cnt)
