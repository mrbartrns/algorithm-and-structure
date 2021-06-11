# 1이 될 때까지
# 더욱 빠르게 풀기 -> 나눗셈 이용
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n, k = map(int, si().split())
ret = 0
while True:
    target = (n // k) * k
    ret += n - target
    n = target
    if n < k:
        break
    ret += 1
    n //= k

ret += n - 1
print(ret)
