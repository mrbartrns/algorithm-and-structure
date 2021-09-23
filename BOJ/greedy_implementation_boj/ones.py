# BOJ 9527 1의 갯수 세기
import sys
import math


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def get_sum(n):
    return n * (n + 1) // 2


a, b = map(int, si().split())
s = get_sum(b) - get_sum(a - 1)
print(get_sum(b) | get_sum(a))
print(bin(get_sum(b) | get_sum(a)))
cnt = 0
s = 0
for i in range(a, b + 1):
    print(i)
    print(bin(i))
    for j in range(56):
        if i & (1 << j):
            cnt += 1
print(cnt)