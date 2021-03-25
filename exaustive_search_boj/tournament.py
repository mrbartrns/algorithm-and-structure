# BOJ 1057
import sys

si = sys.stdin.readline

# 토너먼트가 올라갈때 n감소 및 모든 순서에 맞게끔 숫자의 재배치가 필요
n, a, b = map(int, si().split())
cnt = 1
while n:
    if (a + 1) // 2 == (b + 1) // 2:
        break
    else:
        a = (a + 1) // 2
        b = (b + 1) // 2
        cnt += 1
        n //= 2

if not n:
    print(-1)
else:
    print(cnt)