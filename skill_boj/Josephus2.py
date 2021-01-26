"""
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
dq = deque([i for i in range(1, N + 1)])
res = []
while dq:
    dq.rotate(-K + 1)
    res.append(str(dq.popleft()))
sys.stdout.write("<" + ", ".join(res) + ">")

# deque rotate는 주어진 배열을 회전시킨다.
"""

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
que = deque([i for i in range(1, n + 1)])


def solve(que):
    ret = []
    while que:
        que.rotate(-k + 1)
        ret.append(str(que.popleft()))
    return ret


sys.stdout.write("<" + ", ".join(solve(que)) + ">")
