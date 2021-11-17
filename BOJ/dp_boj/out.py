# BOJ 15486 퇴사2
import sys

sys.setrecursionlimit(10000000)
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def max_value(day):
    if day >= N:
        return 0
    if cache[day] > -1:
        return cache[day]
    cache[day] = 0
    if day + t[day] <= N:
        cache[day] = p[day] + max_value(day + t[day])
    if day + 1 <= N:
        cache[day] = max(cache[day], max_value(day + 1))
    return cache[day]


N = int(si())
t = []
p = []
cache = [-1] * N
for _ in range(N):
    tt, pp = map(int, si().split(" "))
    t.append(tt)
    p.append(pp)
max_value(0)
print(cache[0])
