# BOJ 2164
import sys
from collections import deque

si = sys.stdin.readline

n = int(si())
que = deque([i for i in range(1, n + 1)])
while len(que) != 1:
    que.popleft()
    if len(que) == 1:
        break
    c = que.popleft()
    que.append(c)
print(que[0])