# BOJ 20061
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
fig = 1

n = int(si())
vector = []
graph = [[[0 for _ in range(2)] for _ in range(4)] for _ in range(10)]
for _ in range(n):
    a, b, c = map(int, si().split())
    vector.append((a, b, c))  # t, y, x


def setting_block(t, y, x):
    if t == 1:
        b_idx = x + 1
        while b_idx < 10 and graph[b_idx][y][0] == 0:
            b_idx += 1
        b_idx -= 1

        g_idx = y + 1
        while g_idx < 10 and graph[g_idx][x][1] == 0:
            g_idx += 1
        g_idx -= 1
        graph[g_idx][x][1] = fig


