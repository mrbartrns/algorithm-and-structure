# BOJ 8980 (택배)
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

n, c = map(int, si().split())
m = int(si())
arr = []
for _ in range(m):
    p, q, r = map(int, si().split())
    arr.append((p, q, r))

tot = [0] * (n + 1)

s = 0
arr.sort(key=lambda x: x[0])
# TODO: 함수 완성하기
for i in range(m - 1):
    dep, arrival, stock = arr[i][0], arr[i][1], arr[i][2]
    s -= tot[dep]
    if arrival <= arr[i + 1][1]:
        if s + stock <= c:
            s += stock
            tot[arrival] += stock
        else:
            left = c - s
            s += left
            tot[arrival] += left
    else:
        if (c - s) - arr[i + 1][2] >= 0:
            pass