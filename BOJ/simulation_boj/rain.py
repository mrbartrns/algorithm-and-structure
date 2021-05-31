# BOJ 14719
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

h, w = map(int, si().split())
block = list(map(int, si().split()))
cnt = 0
for i in range(w):
    left = 0
    right = 0
    for j in range(i):
        left = max(left, block[j])
    for j in range(i + 1, w):
        right = max(right, block[j])
    minimum_height = min(left, right)
    if minimum_height - block[i] > 0:
        cnt += minimum_height - block[i]

print(cnt)
print(1 << 32)
