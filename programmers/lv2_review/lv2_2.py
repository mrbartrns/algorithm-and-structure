# 프린터 (스택)
from collections import deque


def solution(priorities, loctation):
    cnt = 1
    que = deque()
    for i in range(len(priorities)):
        que.append((priorities[i], i))
    while que:
        v, idx = que.popleft()
        if not que or (v >= max(que)[0] and idx == loctation):
            return cnt

        if v >= max(que)[0]:
            cnt += 1
        else:
            que.append((v, idx))


p = [3, 3, 4, 2]
l = 3
print(solution(p, l))
