# BOJ 6064
import sys

si = sys.stdin.readline


# 방법 1. 최소공배수를 이용하기
def gcd(a: int, b: int) -> int:
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


# nice
# 최소공배수 구하기
def lcm(a: int, b: int):
    return a * b // gcd(a, b)


t = int(si())
for _ in range(t):
    m, n, x, y = map(int, si().split())
    max_year = lcm(m, n)
    while 1:
        if x > max_year or (x - 1) % n + 1 == y:
            break
        x += m

    if x > max_year:
        print(-1)
    else:
        print(x)
