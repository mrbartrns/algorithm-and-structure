# [카카오] 실패율
from bisect import bisect_left, bisect_right


def solution(n, stages):
    q = []
    stages.sort()
    tot = len(stages)
    for i in range(1, n + 1):
        cnt = bisect_right(stages, i) - bisect_left(stages, i)
        if tot > 0:
            q.append((cnt / tot, i))
        else:
            q.append((0, i))
        tot -= cnt
    q.sort(key=lambda x: (-x[0], x[1]))
    return list(map(lambda x: x[1], q))


if __name__ == "__main__":
    n = 5
    stages = [4, 4, 4, 4, 4]
    print(solution(n, stages))