# BOJ 1026 보물
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


N = int(si())
A = list(map(int, si().split(" ")))
B = list(map(int, si().split(" ")))
A.sort(key=lambda x: -x)
B.sort()
ret = 0
for i in range(N):
    ret += A[i] * B[i]
print(ret)
