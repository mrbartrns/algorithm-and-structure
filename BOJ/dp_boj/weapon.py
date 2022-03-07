# BOJ 18430 무기 공학
from itertools import combinations
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


max_value = [0]
N, M = map(int, si().strip().split(" "))
arr = [list(map(int, si().strip().split(" "))) for _ in range(N)]
base = [(i, j) for i in range(N) for j in range(M)]
print(len(list(combinations(base, (N * M) // 3 + 1))))
ret = []


def backtrack(arr):
    if len(arr) == (N * M) // 3:
        ret.append(arr[:])
        return
    for i in range(4):
        arr.append(i)
        backtrack(arr)
        arr.pop()


backtrack([])
print(len(ret))
