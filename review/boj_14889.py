# BOJ 14889
import sys
from itertools import combinations

si = sys.stdin.readline


def psum(team):
    s = 0
    for i in team:
        for j in team:
            s += graph[i][j]
    return s


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
people = [i for i in range(n)]
# 모든 반으로 쪼갠 경우에 대해서 고려된다.
team = list(combinations(people, n // 2))
size = len(team)
start = team[: size // 2]
link = list(reversed(team[size // 2 :]))
MIN = 10000000
print(start)
print(link)

for i in range(size // 2):
    s_team = start[i]
    l_team = link[i]
    s_s = psum(s_team)
    l_s = psum(l_team)
    if abs(s_s - l_s) < MIN:
        MIN = abs(s_s - l_s)

print(MIN)
