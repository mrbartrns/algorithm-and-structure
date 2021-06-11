# 1이 될 때까지
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n, k = map(int, si().split())
cnt = 0
while n > 1:
    while n % k == 0:
        n //= k
        cnt += 1
    if n == 1:
        break
    cnt += (n % k)
    n -= (n % k)
print(cnt)
