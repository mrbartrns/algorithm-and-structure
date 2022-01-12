# BOJ 2591 숫자카드
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline


def divide(start):
    if start >= N:
        return 1
    if int(STR_N[start]) == 0:
        return 0
    if cache[start] > -1:
        return cache[start]
    cache[start] = 0
    for end in range(start + 1, N + 1):
        if 1 <= int(STR_N[start:end]) <= 34:
            cache[start] += divide(end)
    return cache[start]


STR_N = si().strip()
N = len(STR_N)
cache = [-1] * N
print(divide(0))
