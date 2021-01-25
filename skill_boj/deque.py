# BOJ 10866
import sys
from collections import deque

si = sys.stdin.readline


n = int(si())
que = deque([])
for _ in range(n):
    op, *data = si().split()
    data = list(map(int, data))
    if op == "push_front":
        que.appendleft(data[0])
    elif op == "push_back":
        que.append(data[0])
    elif op == "pop_front":
        print(que.popleft() if que else -1)
    elif op == "pop_back":
        print(que.pop() if que else -1)
    elif op == "size":
        print(len(que))
    elif op == "empty":
        print(0 if que else 1)
    elif op == "front":
        print(que[0] if que else -1)
    elif op == "back":
        print(que[-1] if que else -1)
