# BOJ 14891 (톱니바퀴)
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def rotate_gears(idx, d):
    visited[idx] = True
    if idx + 1 < 4 and not visited[idx + 1] and gears[idx][2] != gears[idx + 1][6]:
        rotate_gears(idx + 1, -d)
    if idx - 1 >= 0 and not visited[idx - 1] and gears[idx][6] != gears[idx - 1][2]:
        rotate_gears(idx - 1, -d)
    gears[idx].rotate(d)


gears = [deque(map(int, list(si().strip()))) for _ in range(4)]
order = []
score = 0
K = int(si())
for _ in range(K):
    a, b = map(int, si().split())
    order.append((a - 1, b))

for i in range(K):
    gear_idx, direction = order[i]
    visited = [False] * 4
    rotate_gears(gear_idx, direction)
    # for j in range(4):
    #     print(gears[j])
    # print()
for i in range(4):
    score += 2 ** i if gears[i][0] == 1 else 0

print(score)
