# BOJ 2616 소형 기관차
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline
INF = 987654321


def get_psum(arr):
    s = 0
    ret = [0]
    for i in range(len(arr)):
        s += arr[i]
        ret.append(s)
    return ret


N = int(si().strip())
arr = list(map(int, si().strip().split(" ")))
M = int(si().strip())
psum = get_psum(arr)
cache = [[-INF for _ in range(len(psum))] for _ in range(3)]


def solve(idx, start):
    if idx >= 3:
        return 0
    if start >= len(psum):
        return -INF
    if cache[idx][start] > -INF:
        return cache[idx][start]
    cache[idx][start] = max(
        psum[start + M] - psum[start] + solve(idx + 1, start + M)
        if start + M < len(psum)
        else -INF,
        solve(idx, start + 1),
    )
    return cache[idx][start]


solve(0, 0)
print(cache[0][0])
