# BOJ 7795 먹을 것인가 먹힐 것인가
"""
원리에 대하여 생각해보기: 어떤 값을 중간값으로 설정해야 하는지?
"""
from bisect import bisect_left
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

T = int(si().strip())
for _ in range(T):
    N, M = map(int, si().split(" "))
    arr1 = list(map(int, si().strip().split(" ")))
    arr2 = list(map(int, si().strip().split(" ")))
    arr2.sort()
    count = 0
    for i in range(N):
        a = bisect_left(arr2, arr1[i])
        count += a
    print(count)
