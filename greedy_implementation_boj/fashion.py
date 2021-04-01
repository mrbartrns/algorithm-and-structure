# BOJ 9375
import sys

si = sys.stdin.readline

t = int(si())
for _ in range(t):
    clothes = {}
    res = 1
    n = int(si())
    for _ in range(n):
        cloth, category = si().split()
        clothes[category] = clothes.get(category, 1) + 1
    for values in clothes.values():
        res *= values
    res -= 1
    print(res)

