# BOJ 2688 줄어들지 않는 숫자
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def solve(idx, start):
    if idx < 0:
        return 1
    if cache[idx][start] > -1:
        return cache[idx][start]
    cache[idx][start] = 0
    for i in range(start, 10):
        cache[idx][start] += solve(idx - 1, i)
    return cache[idx][start]


cache = [[-1 for _ in range(10)] for _ in range(65)]
solve(64, 0)
T = int(si().strip())
for _ in range(T):
    N = int(si().strip())
    print(cache[N - 1][0])
