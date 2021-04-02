# BOJ 9517
import sys

si = sys.stdin.readline

k = int(si())
n = int(si())
limit = 210
idx = k - 1
done = False
for _ in range(n):
    str_time, check = si().split()
    t = int(str_time)
    limit -= t
    if not done and limit <= 0:
        print(idx + 1)
        done = True
    if check == 'T':
        idx = (idx + 1) % 8
