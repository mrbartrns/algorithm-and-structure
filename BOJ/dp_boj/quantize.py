# 양자화
from itertools import combinations
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def quantize(idx, digit_set):
    if idx == len(arr):
        return 0
    ret = INF
    for quan in digit_set:
        ret = min(ret, (quan - arr[idx]) ** 2 + quantize(idx + 1, digit_set))
    return ret


T = int(si())
for _ in range(T):
    N, K = map(int, si().split(" "))
    arr = list(map(int, si().split(" ")))
    kinds = list(set(arr))
    answer = INF
    for i in range(K if K <= len(kinds) else len(kinds)):
        comb = list(combinations(kinds, i + 1))
        for c in comb:
            answer = min(answer, quantize(0, c))
    print(answer)
