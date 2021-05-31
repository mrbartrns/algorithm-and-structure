# BOJ 17822
"""
1. 번호가 Xi의 배수인 원판을 di 방향으로 k칸 회전시키기 (if d == 0: clockwise, elif d == 1: counter clockwise)
2. 원판에 수가 남아있으면, 인접하면서 수가 같은것을 모두 찾기
2-1. 수가 있는 경우 지우기
2-2. 없는 경우 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고 작은수에는 1을 더하기
수정 완료
"""
import sys
from collections import deque
from functools import reduce

si = sys.stdin.readline


def rotate(p, r):
    for i in range(p, n + 1, p):
        plate[i - 1].rotate(r)


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
                que.append((ny, nx))
                plate[ny][nx] = 0
                flag = True
    return flag


def get_average():
    s = 0
    cnt = 0
    for y in range(n):
        for x in range(m):
            if plate[y][x] > 0:
                cnt += 1
                s += plate[y][x]
    return s / cnt if cnt > 0 else -1


n, m, t = map(int, si().split())

# move_dir
dy = [-1, 1, 0, 0]
dx = [0, 0, m - 1, 1]

rotation = []
plate = [deque(list(map(int, si().split()))) for _ in range(n)]
for _ in range(t):
    a, b, c = map(int, si().split())
    if b == 0:  # clockwise
        rotation.append((a, c))
    else:  # counter-clockwise
        rotation.append((a, -c))

res = 0

for p, r in rotation:
    rotate(p, r)
    get_ave_cnt = 0
    for i in range(n):
        for j in range(m):
            if plate[i][j] > 0:
                if bfs(i, j, plate[i][j]):
                    get_ave_cnt += 1

    if not get_ave_cnt:
        ave = get_average()
        if ave == -1:
            pass
        for i in range(n):
            for j in range(m):
                if plate[i][j] == 0:
                    continue
                if plate[i][j] > ave:
                    plate[i][j] -= 1
                elif plate[i][j] < ave:
                    plate[i][j] += 1

for i in range(n):
    res += reduce(lambda acc, cur: acc + cur, plate[i], 0)
print(res)
