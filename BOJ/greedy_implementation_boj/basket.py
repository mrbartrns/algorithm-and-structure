# BOJ 10813
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
basket = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, si().split())
    basket[a], basket[b] = basket[b], basket[a]

for i in range(1, n + 1):
    print(basket[i], end=" ")
