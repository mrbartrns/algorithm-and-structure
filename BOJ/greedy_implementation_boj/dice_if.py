# BOJ 2480 주사위 세개
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def calculate(d1, d2, d3):
    if d1 == d2 and d2 == d3 and d3 == d1:
        return 10000 + d1 * 1000
    elif d1 == d2:
        return 1000 + 100 * d1
    elif d2 == d3:
        return 1000 + 100 * d2
    elif d3 == d1:
        return 1000 + 100 * d3
    else:
        return max(d1, d2, d3) * 100


a, b, c = map(int, si().strip().split(" "))
print(calculate(a, b, c))
