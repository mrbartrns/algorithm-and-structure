# BOJ 2591 숫자 카드
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def in_range(number):
    return 0 <= number <= 34


STR_N = si().strip()
N = len(STR_N)
cache = [0] * (N + 1)
cache[0] = 1
for i in range(1, N + 1):
    if i - 1 >= 0 and int(STR_N[i - 1]) != 0 and in_range(int(STR_N[i - 1 : i])):
        cache[i] += cache[i - 1]
    if i - 2 >= 0 and int(STR_N[i - 2]) != 0 and in_range(int(STR_N[i - 2 : i])):
        cache[i] += cache[i - 2]
print(cache[N])
