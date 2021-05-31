# BOJ 1850
import sys

input = sys.stdin.readline


def get_gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    val = get_gcd(b, a % b)
    return val


def transform(n):
    num = "1" * n
    return int(num)


a, b = map(int, input().split())
gcd = get_gcd(a, b)
print("1" * gcd)