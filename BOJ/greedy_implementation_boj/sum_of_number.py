# BOJ 1789 (수들의 합)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def sum_of_number(n):
    return n * (n + 1) // 2


n = int(si())
i = 0
while True:
    if sum_of_number(i) <= n < sum_of_number(i + 1):
        print(i)
        break
    i += 1
