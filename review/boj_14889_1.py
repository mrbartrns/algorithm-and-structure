# BOJ 14889 (스타트와 링크)
import sys
from itertools import combinations

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321


def psum(team):
    s = 0
    for i in team:
        for j in team:
            s += graph[i][j]
    return s


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
people_ = [i for i in range(n)]
res = INF

teams = list(combinations(people_, n // 2))

for i in range(len(teams) // 2):
    start = teams[i]
    link = teams[len(teams) - 1 - i]
    start_sum = psum(start)
    link_sum = psum(link)
    res = min(res, abs(start_sum - link_sum))
print(res)
