# BOJ 14891
import sys
from collections import deque

"""
1번 톱니바퀴 열두시 방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴 열두시 방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴 열두시 방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴 열두시방향이 N극이면 0점, S극이면 8점
N극: 0, S극: 1
2번과 6번에 대해서 확인할것
방향1: 시계방향 -1: 반시계 방향
"""


def rotate(idx, direction):
    visited[idx] = True
    this = gears[idx]
    left = False
    right = False
    if idx - 1 >= 0 and this[6] != gears[idx - 1][2]:
        left = True
    if idx + 1 < 4 and this[2] != gears[idx + 1][6]:
        right = True

    if direction == -1:
        el = this.popleft()
        this.append(el)
    elif direction == 1:
        el = this.pop()
        this.appendleft(el)

    if idx - 1 >= 0 and not visited[idx - 1] and left:
        rotate(idx - 1, -direction)
    if idx + 1 < 4 and not visited[idx + 1] and right:
        rotate(idx + 1, -direction)


si = sys.stdin.readline
gears = []
res = 0
for _ in range(4):
    temp = list(map(int, si().strip()))
    que = deque(temp)
    gears.append(que)

n = int(si())
for _ in range(n):
    visited = [False] * 4
    x, d = map(int, si().split())
    rotate(x - 1, d)

for i in range(4):
    res += (2 ** i) * gears[i][0]

print(res)
