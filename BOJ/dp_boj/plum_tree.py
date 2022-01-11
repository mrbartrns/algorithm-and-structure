# BOJ 2240 자두 나무
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(100000)
si = sys.stdin.readline


def eat(t, w, x):
    if t >= T:
        return 0
    if cache[t][w][x] > -1:
        return cache[t][w][x]
    cache[t][w][x] = 0
    if plums[t] == x:
        if w < W:
            cache[t][w][x] = max(
                cache[t][w][x], 1 + eat(t + 1, w, x), eat(t + 1, w + 1, 1 - x)
            )
        else:
            cache[t][w][x] = max(cache[t][w][x], 1 + eat(t + 1, w, x))
    else:
        if w < W:
            cache[t][w][x] = max(
                cache[t][w][x], eat(t + 1, w, x), 1 + eat(t + 1, w + 1, 1 - x)
            )
        else:
            cache[t][w][x] = max(cache[t][w][x], eat(t + 1, w, x))
    return cache[t][w][x]


T, W = map(int, si().strip().split(" "))
plums = []
cache = [[[-1 for _ in range(2)] for _ in range(W + 1)] for _ in range(T)]
for _ in range(T):
    plums.append(int(si().strip()) - 1)
print(eat(0, 0, 0))
