# BOJ 17779
"""
선거구를 선정하는 방법
가장 윗 점인 x, y를 선정 (1 <= x <= N, 1 <= y <= N)
d1, d2를 이용하여 구획 쪼개기 (d1, d2는 브루트포스를 이용하여 모두 선정하기, d1, d2 >= 1)
x, y 정하기 1 <= x < x + d1 + d2 <= N
1. x, y의 위치를 정하기
"""
import sys

si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def label_5(y, x, d1, d2):
    i = 0
    while i <= d1:
        label[y + i][x - i] = 5
        i += 1
    i = 0
    while i <= d2:
        label[y + i][x + i] = 5
        i += 1
    i = 0
    while i <= d2:
        label[y + d1 + i][x - d1 + i] = 5
        i += 1
    i = 0
    while i <= d1:
        label[y + d2 + i][x + d2 - i] = 5
        i += 1

    # 5 labeling
    flag = True
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i < y:
                continue
            if i == y and j < x:
                continue
            if i == y + d1 + d2 and j == x + d2 - d1:
                break
            if label[i][j] == 5:
                flag = not flag
            elif flag:
                label[i][j] = 5


# 1, 2, 3, 4 labeling
def labeling(y, x, d1, d2):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if label[i][j] == 5:
                continue
            if 1 <= i < y + d1 and 1 <= j <= x:
                label[i][j] = 1
            elif 1 <= i <= y + d2 and x < j <= n:
                label[i][j] = 2
            elif y + d1 <= i <= n and 1 <= j < x - d1 + d2:
                label[i][j] = 3
            elif y + d2 < i <= n and x - d1 + d2 <= j <= n:
                label[i][j] = 4


n = int(si())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i] = [0] + list(map(int, si().split()))

res = 987654321
boundary = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if not (1 <= i <= i + d1 + d2 <= n):
                    continue
                if not (1 <= j - d1 <= j <= j + d2 <= n):
                    continue
                boundary.append((i, j, d1, d2))

for i in range(len(boundary)):
    label = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    s1, s2, s3, s4, s5 = 0, 0, 0, 0, 0
    max_val = 0
    min_val = 987654321
    r, c, d1, d2 = boundary[i]
    label_5(r, c, d1, d2)
    labeling(r, c, d1, d2)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if label[i][j] == 1:
                s1 += graph[i][j]
            elif label[i][j] == 2:
                s2 += graph[i][j]
            elif label[i][j] == 3:
                s3 += graph[i][j]
            elif label[i][j] == 4:
                s4 += graph[i][j]
            elif label[i][j] == 5:
                s5 += graph[i][j]
    max_val = max(s1, s2, s3, s4, s5)
    min_val = min(s1, s2, s3, s4, s5)
    res = min(max_val - min_val, res)

print(res)
