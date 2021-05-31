# BOJ 17822 (원판 돌리기)
import sys
from collections import deque
from functools import reduce

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def rotate(p, k):
    for i in range(p, n + 1, p):
        plate[i - 1].rotate(k)


def bfs(y, x, k):
    que = deque()
    que.append((y, x))
    flag = False
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = (x + dx[i]) % m
            if ny < 0 or ny >= n:
                continue
            if plate[ny][nx] == k:
                plate[ny][nx] = 0
                que.append((ny, nx))
                flag = True
    return flag


def get_average():
    s = 0
    cnt = 0
    for y in range(n):
        for x in range(m):
            if plate[y][x] > 0:
                s += plate[y][x]
                cnt += 1
    return s / cnt if cnt > 0 else -1


n, m, t = map(int, si().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, m - 1, 1]
plate = [deque(list(map(int, si().split()))) for _ in range(n)]
order = []
for _ in range(t):
    a, b, c = map(int, si().split())
    if b == 0:
        order.append((a, c))
    else:
        order.append((a, -c))

for i in range(t):
    p, k = order[i]  # plate 배수, 돌려야 할 칸의 수
    rotate(p, k)
    chk = False
    for i in range(n):
        for j in range(m):
            if plate[i][j] > 0:
                if bfs(i, j, plate[i][j]):
                    chk = True
    if not chk:
        ave = get_average()
        if ave > -1:
            for i in range(n):
                for j in range(m):
                    if plate[i][j] > 0:
                        if plate[i][j] < ave:
                            plate[i][j] += 1
                        elif plate[i][j] > ave:
                            plate[i][j] -= 1
score = 0
for i in range(n):
    score += reduce(lambda acc, cur: acc + cur, plate[i], 0)
print(score)
