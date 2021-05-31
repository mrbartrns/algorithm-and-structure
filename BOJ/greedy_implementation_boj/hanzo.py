# BOJ 14659
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
val = 0
cnt = 0
res = 0
for i in range(n):
    if val < arr[i]:
        val = arr[i]
        res = max(res, cnt)
        cnt = 0
    else:
        cnt += 1
res = max(res, cnt)
print(res)
