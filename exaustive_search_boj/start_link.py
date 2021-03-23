# BOJ 14889
import sys
from itertools import combinations

si = sys.stdin.readline

n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
people = [i for i in range(n)]
comb = list(combinations(people, n // 2))
size = len(comb)
start = comb[: size // 2]
link = list(reversed(comb[size // 2 :]))

sub = 10000000
for i in range(size // 2):
    s_couple = start[i]
    l_couple = link[i]
    s_s = 0
    l_s = 0
    for j in s_couple:
        for k in s_couple:
            s_s += graph[j][k]

    for j in l_couple:
        for k in l_couple:
            l_s += graph[j][k]
    if sub > abs(s_s - l_s):
        sub = abs(s_s - l_s)

print(sub)
