# BOJ 11723
import sys

si = sys.stdin.readline
n = int(si())
numbers = set()
number = -1
for _ in range(n):
    ops = list(si().split())
    op = ops[0]
    if len(ops) > 1:
        number = int(ops[1])
    if op == "add":
        numbers.add(number)
    elif number in numbers and op == "remove":
        numbers.remove(number)
    elif op == "check":
        print(1 if number in numbers else 0)
    elif op == "toggle":
        if number in numbers:
            numbers.remove(number)
        else:
            numbers.add(number)
    elif op == "all":
        numbers = set([i for i in range(1, 21)])
    elif op == "empty":
        numbers = set()
