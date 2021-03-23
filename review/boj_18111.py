# BOJ 18111
import sys

si = sys.stdin.readline
n, m, inv = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
MIN = 256
MAX = -1
time = 1e15
block_height = 1e15
for i in range(n):
    for j in range(m):
        if graph[i][j] < MIN:
            MIN = graph[i][j]
        if graph[i][j] > MAX:
            MAX = graph[i][j]


# MIN과 MAX 사이의 값을 돌면서 탐색
for i in range(MIN, MAX + 1):
    inventory = inv
    t = 0
    for x in range(n):
        for y in range(m):
            height = graph[x][y] - i
            # 기준치보다 작다면 인벤토리에서 꺼내기
            if height < 0:
                inventory += height
                t -= height
            # 기준치보다 크다면 블록을 제거하기
            elif height > 0:
                t = 2 * height
                # inventory에 빼낸 블록을 저장
                inventory += height
    if inventory >= 0:
        if t <= time:
            block_height = i
            time = t

print(time, block_height)
