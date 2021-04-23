# BOJ 4796
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

t = 0
while True:
    t += 1
    l, p, v = map(int, si().split())
    ans = v
    if l == p == v == 0:
        break
    ans -= (v // p) * (p - l)
    if v - (v // p) * p > l:
        ans -= v - (v // p) * p - l
    print(f"Case {t}: {ans}")
