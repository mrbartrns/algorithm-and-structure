# BOJ 9517
import sys

si = sys.stdin.readline

k = int(si())
n = int(si())
limit = 210
arr = [0] * 8
idx = k - 1
for _ in range(n):
    str_time, check = si().split()
    t = int(str_time)
    if check == 'T':
        idx = (idx + 1) % 8
    limit -= t
    if limit <= 0:
        print(idx + 1)