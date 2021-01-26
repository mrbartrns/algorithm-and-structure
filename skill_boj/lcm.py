# BOJ 1934
import sys

input = sys.stdin.readline


def get_gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    val = get_gcd(b, a % b)
    return val


def get_lcm(a, b):
    gcd = get_gcd(a, b)
    return a * b // gcd


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(get_lcm(a, b))