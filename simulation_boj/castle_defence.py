# BOJ 17135
import copy
import sys
from itertools import combinations

si = sys.stdin.readline

n, m, d = map(int, si().split())
maps = [list(map(int, si().split())) for _ in range(n)]
arch = list(combinations([i for i in range(m)], 3))
killed = 0

# 1. 궁수의 위치를 정하기
for c in range(len(arch)):
    location = [(n, arch[c][0]), (n, arch[c][1]), (n, arch[c][2])]
    graph = copy.deepcopy(maps)
    cnt = 0
    while True:
        # check = []
        enemy = []

        # 2. 적들의 위치를 왼쪽부터 차례대로 넣기
        for j in range(m):
            for i in range(n):
                if graph[i][j] == 1:
                    enemy.append((i, j))

        if not len(enemy):
            killed = max(killed, cnt)
            break

        # 2. 공격 -> 모든 적 배열을 탐색하여 check에 없애야 할 적을 추가하기
        for i in range(3):
            distance = d + 1
            cur_y, cur_x = -1, -1
            for j in range(len(enemy)):
                y1, x1 = location[i]
                y2, x2 = enemy[j]
                dist = abs(y1 - y2) + abs(x1 - x2)
                if dist < distance:
                    distance = dist
                    cur_y = y2
                    cur_x = x2
            # check.append((cur_y, cur_x))
            if cur_y > -1 and cur_x > -1:
                graph[cur_y][cur_x] = 0
                cnt += 1

        # 3. 적의 이동
        for j in range(m - 1, -1, -1):
            for i in range(1, n):
                graph[i][j] = graph[i - 1][j]

print(killed)
