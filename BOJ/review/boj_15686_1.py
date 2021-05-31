# BOJ 15686 (치킨 배달)
import sys
from itertools import combinations

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321

n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
houses = []
locations = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            locations.append((i, j))
chickens = list(combinations(locations, m))
distance = INF
for i in range(len(chickens)):
    chicken = chickens[i]
    s = 0
    for j in range(len(houses)):
        c = INF
        y1, x1 = houses[j]
        for k in range(m):
            y2, x2 = chicken[k]
            c = min(c, abs(x1 - x2) + abs(y1 - y2))
        s += c
    distance = min(distance, s)
print(distance)
