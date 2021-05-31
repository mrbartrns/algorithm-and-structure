# BOJ 1120
import sys

si = sys.stdin.readline
a, b = map(str, si().split())
s = 51

for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if b[i + j] != a[j]:
            cnt += 1
    s = min(s, cnt)
print(s)