# BOJ 2229 팀 짜기
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(10000000)
si = sys.stdin.readline


def make_team(start):
    if start >= N:
        return 0
    if cache[start] > -1:
        return cache[start]
    cache[start] = 0
    max_value = arr[start]
    min_value = arr[start]
    for end in range(start, N):
        max_value = max(max_value, arr[end])
        min_value = min(min_value, arr[end])
        cache[start] = max(cache[start], max_value - min_value + make_team(end + 1))
    return cache[start]


N = int(si().strip())
arr = list(map(int, si().strip().split(" ")))
cache = [-1] * N
print(make_team(0))
