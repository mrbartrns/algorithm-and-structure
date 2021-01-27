# BOJ 2745 진법변환 연습
import sys

si = sys.stdin.readline

n, l = si().split()
n = n.strip()
l = int(l)

k = len(n) - 1


def solve(n, k, l):
    num = 0
    if not n:
        return 0
    if ord(n[0]) >= ord("A"):
        num = (ord(n[0]) - ord("A") + 10) * (l ** k) + solve(n[1:], k - 1, l)
    else:
        num = int(n[0]) * (l ** k) + solve(n[1:], k - 1, l)
    return num


print(solve(n, k, l))
print(ord("Z") - ord("A"))
# print(ord("0"), ord("9"), ord("A"))
