# 기능개발
from collections import deque


def solution(progress, speeds):
    res = []
    que = deque(progress)
    speeds_que = deque(speeds)
    while que:
        cnt = 0
        for i in range(len(que)):
            que[i] += speeds_que[i]

        while que and que[0] >= 100:
            que.popleft()
            speeds_que.popleft()
            cnt += 1

        if cnt > 0:
            res.append(cnt)
    return res


progress = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progress, speeds))