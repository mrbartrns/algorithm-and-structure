# BOJ 14888 (연산자 끼워넣기)
import sys
from itertools import permutations

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
MAX = int(1e12)
MIN = -int(1e12)


def solve(numbers, operations):
    ret = numbers[0]
    for i in range(1, n):
        number = numbers[i]
        sign = operations[i - 1]
        if sign == "+":
            ret += number
        elif sign == "-":
            ret -= number
        elif sign == "*":
            ret *= number
        else:
            if ret > 0:
                ret //= number
            else:
                temp = abs(ret)
                temp //= number
                ret = -temp
    return ret


n = int(si())
numbers = list(map(int, si().split()))
op_number = list(map(int, si().split()))
ops = []
for i in range(4):
    if op_number[i] > 0:
        for _ in range(op_number[i]):
            if i == 0:
                ops.append("+")
            elif i == 1:
                ops.append("-")
            elif i == 2:
                ops.append("*")
            else:
                ops.append("/")

perms = permutations(ops)
min_value = MAX
max_value = MIN
for signs in perms:
    res = solve(numbers, signs)
    min_value = min(min_value, res)
    max_value = max(max_value, res)
print(max_value)
print(min_value)
