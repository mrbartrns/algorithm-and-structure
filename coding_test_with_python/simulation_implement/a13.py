# BOJ 15686 치킨 배달
import sys
from itertools import combinations

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321

n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        if graph[i][j] == 2:
            chicken.append((i, j))

chicken_comb = list(combinations(chicken, m))
answer = INF
for chickens in chicken_comb:
    res = 0
    for y, x in house:
        minimum = INF
        for cy, cx in chickens:
            minimum = min(minimum, abs(cy - y) + abs(cx - x))
        res += minimum
    answer = min(answer, res)
print(answer)
