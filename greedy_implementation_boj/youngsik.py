# BOJ 1592
import sys

si = sys.stdin.readline

n, m, l = map(int, si().split())
arr = [0] * n
idx = 0
cnt = 0
while True:
    arr[idx] += 1
    if arr[idx] == m:
        break
    if arr[idx] % 2 == 1:
        idx = (idx + l) % n
    else:
        idx = (idx + n - l) % n
    cnt += 1
print(cnt)
