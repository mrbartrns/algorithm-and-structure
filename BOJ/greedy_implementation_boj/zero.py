# BOJ 10773
import sys

si = sys.stdin.readline

n = int(si())
s = 0
stack = []
for _ in range(n):
    number = int(si())
    if number > 0:
        stack.append(number)
        s += number
    else:
        c = stack.pop()
        s -= c

print(s)