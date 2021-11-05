# BOJ 1461
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def push_value(arr, m):
    for i in range(0, len(arr), m):
        ret.append(abs(arr[i]))


N, M = map(int, si().split(" "))
arr = list(map(int, si().split(" ")))
plus = []
minus = []
for i in range(N):
    if arr[i] < 0:
        minus.append(arr[i])
    else:
        plus.append(arr[i])

ret = []
minus.sort(key=lambda x: -abs(x))
plus.sort(key=lambda x: -abs(x))
push_value(minus, M)
push_value(plus, M)
ret.sort()
if len(ret) == 1:
    print(ret[0])
else:
    print(2 * sum(ret) - ret[-1])
