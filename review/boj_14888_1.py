# BOJ 14888 (연산자 끼워넣기)
import sys
from itertools import permutations

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 1e15


def operate(prev, cur, op):
    if op == 0:
        return prev + cur
    elif op == 1:
        return prev - cur
    elif op == 2:
        return prev * cur
    else:
        if prev < 0:
            return -(abs(prev) // cur)
        return prev // cur


n = int(si())
numbers = list(map(int, si().split()))
op_list = list(map(int, si().split()))
operators = []
for i in range(4):
    val = op_list[i]
    for _ in range(val):
        operators.append(i)

max_val = -INF
min_val = INF
operators_iter = list(permutations(operators))
for ops in operators_iter:
    temp = numbers[0]
    for i in range(1, n):
        temp = operate(temp, numbers[i], ops[i - 1])
    max_val = max(max_val, temp)
    min_val = min(min_val, temp)
print(max_val)
print(min_val)
