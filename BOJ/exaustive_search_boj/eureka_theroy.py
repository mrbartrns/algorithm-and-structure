# BOJ 10448
import sys

si = sys.stdin.readline

number_list = []
for i in range(1, 1001):
    number_list.append((i * (i + 1)) // 2)


def backtrack(n, k, number):
    if n == k:
        if number == 0:
            return True
        return False

    for i in range(len(number_list)):
        tri = number_list[i]
        if tri <= number and backtrack(n, k + 1, number - tri):
            return True
        if tri > number:
            break
    return False


t = int(si())
for _ in range(t):
    n = int(si())
    if backtrack(3, 0, n):
        print(1)
    else:
        print(0)