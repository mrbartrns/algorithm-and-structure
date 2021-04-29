# BOJ 2812
import sys

# sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

cnt = 0
n, k = map(int, si().split())
char = si().strip()
stack = []
for c in char:
    while stack and int(stack[-1]) < int(c) and cnt < k:
        stack.pop()
        cnt += 1
    stack.append(c)

while stack and cnt < k:
    stack.pop()
    cnt += 1

print("".join(stack))
