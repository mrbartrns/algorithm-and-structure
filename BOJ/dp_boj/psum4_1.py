# BOJ 11659
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
arr = [0] + list(map(int, si().split()))
s = 0
psum = []
for i in range(n + 1):
    s += arr[i]
    psum.append(s)

for _ in range(m):
    a, b = map(int, si().split())
    print(psum[b] - psum[a - 1])
