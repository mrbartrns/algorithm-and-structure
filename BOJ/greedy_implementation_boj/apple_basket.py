# BOJ 2828
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
n, m = map(int, si().split())
j = int(si())
left = 1
right = m
arr = [int(si()) for _ in range(j)]
ans = 0

for i in range(j):
    res = 0
    if arr[i] < left or arr[i] > right:
        res = min(abs(arr[i] - left), abs(arr[i] - right))
    ans += res

print(ans)
