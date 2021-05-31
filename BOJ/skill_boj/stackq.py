# BOJ 10828
import sys

si = sys.stdin.readline


n = int(si())
stack = []
for _ in range(n):
    op, *data = si().split()
    data = list(map(int, data))
    if op == "push":
        stack.append(data[0])
    elif op == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif op == "size":
        print(len(stack))
    elif op == "empty":
        print(1 if not stack else 0)
    elif op == "top":
        print(-1 if not stack else stack[-1])