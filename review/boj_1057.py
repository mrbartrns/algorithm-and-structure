# BOJ 1057
import sys

si = sys.stdin.readline
n, a, b = map(int, si().split())
cnt = 1
while n:
    if (a + 1) // 2 == (b + 1) // 2:
        break
    else:
        a = (a + 1) // 2
        b = (b + 1) // 2
        n //= 2
        cnt += 1

print(cnt) if n else print(-1)