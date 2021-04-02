# BOJ 10810
import sys


si = sys.stdin.readline

n, m = map(int, si().split())
balls = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, si().split())
    for i in range(a, b + 1):
        balls[i] = c

for i in range(1, n + 1):
    print(balls[i], end=" ")

# test
