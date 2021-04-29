# BOJ 2212
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n = int(si())
k = int(si())
arr = list(map(int, si().split()))

if n <= k:
    print(0)
else:
    arr.sort()
    diff = []
    for i in range(1, n):
        diff.append(arr[i] - arr[i - 1])
    diff.sort()
    res = 0
    for i in range(n - k):
        res += diff[i]
    print(res)
