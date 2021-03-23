# BOJ 18111
# 리모컨과 비슷한 문제
import sys

"""
브루트 포스를 이용하는법: min, max 사이의 값을 모두 조절하여 확인하기 -> 시간이 걸려도 
"""
si = sys.stdin.readline
n, m, inventory = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
min_q = []
max_q = []
MIN = 50000
MAX = -1
res = 100000000000000
block_height = 500000000000000

for i in range(n):
    for j in range(m):
        if graph[i][j] < MIN:
            MIN = graph[i][j]
        if graph[i][j] > MAX:
            MAX = graph[i][j]


# 모든 그래프의 칸에 대해 min, max사이의 숫자 사이에 어떤 관계를 갖는지 확인하기
for i in range(MIN, MAX + 1):
    time = 0
    block = inventory
    for x in range(n):
        for y in range(m):
            height = graph[x][y] - i
            if height > 0:
                time += height * 2
                block += height
            elif height < 0:
                time -= height
                block += height
    if block >= 0:
        if time <= res:
            res = time
            block_height = i

print(res, block_height)