# BOJ 11052
import sys

input = sys.stdin.readline


def solve(n):
    for i in range(2, n + 1):
        d[i] = packs[i - 1]
        for j in range(i):
            d[i] = max(d[i], d[i - j] + d[j])
    return d[n]


n = int(input())
packs = list(map(int, input().split()))
d = [0] * (n + 1)
d[1] = packs[0]
print(solve(n))