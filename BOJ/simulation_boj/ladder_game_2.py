# BOJ 15684
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n, m, h = map(int, si().split())

ladder = [[False for _ in range(n - 1)] for _ in range(h)]

for _ in range(m):
    a, b = map(int, si().split())
    ladder[a - 1][b - 1] = True

for i in range(h):
    for j in range(n - 1):
        print(ladder[i][j], end=" ")
    print()

res = 0
for j in range(n - 1):
    cnt = 0
    for i in range(h):
        if ladder[i][j]:
            cnt += 1
    if cnt % 2 == 1:
        res += 1

print(res if res <= 3 else -1)
