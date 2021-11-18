# BOJ 15989 1, 2, 3 더하기 4
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

T = int(si())
cache = [0] * 10001
cache[0] = 1
for cnt in range(1, 4):
    for i in range(1, 10001):
        if i - cnt >= 0:
            cache[i] += cache[i - cnt]
for _ in range(T):
    N = int(si())
    print(cache[N])
