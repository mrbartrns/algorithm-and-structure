# BOJ 1406
import sys
from collections import deque

si = sys.stdin.readline


word = si().strip()
ans = word
left = deque(list(word))
right = deque([])
idx = len(ans)
n = int(si())

for i in range(n):
    op, *a = si().split()
    if op == "L" and left:
        c = left.pop()
        right.appendleft(c)
    elif op == "D" and right:
        c = right.popleft()
        left.append(c)
    elif op == "B" and left:
        left.pop()
    elif op == "P":
        left.append(a[0])
print("".join(left) + "".join(right))
