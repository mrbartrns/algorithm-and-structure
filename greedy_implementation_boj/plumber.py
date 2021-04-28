# BOJ 1449
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

n, m = map(int, si().split())
arr = list(map(int, si().split()))
arr.sort()
s = arr[0]
res = 1
for i in range(n):
    if arr[i] - s + 1 > m:
        s = arr[i]
        res += 1

print(res)
