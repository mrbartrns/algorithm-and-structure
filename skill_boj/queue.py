# BOJ 10845
import sys
from collections import deque

si = sys.stdin.readline


que = deque([])
n = int(si())
for _ in range(n):
    op, *data = si().split()
    data = list(map(int, data))
    if op == "push":
        que.append(data[0])
    elif op == "pop":
        if que:
            c = que.popleft()
            print(c)
        else:
            print(-1)
    elif op == "size":
        print(len(que))
    elif op == "empty":
        print(1 if not que else 0)
    elif op == "front":
        print(que[0] if que else -1)
    elif op == "back":
        print(que[-1] if que else -1)