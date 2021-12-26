# BOJ 2502 떡 먹는 호랑이
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def get_value():
    for i in range(1, K + 1):
        spare = K - (first[D] * i)
        if spare % second[D] == 0:
            return i, spare // second[D]


D, K = map(int, si().strip().split(" "))
first = [0] * (D + 1)
second = [0] * (D + 1)
first[1] = 1
second[2] = 1
for i in range(3, D + 1):
    first[i] = first[i - 1] + first[i - 2]
    second[i] = second[i - 1] + second[i - 2]
a, b = get_value()
print(a)
print(b)
