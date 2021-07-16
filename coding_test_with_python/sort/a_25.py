# [카카오] 실패율
import heapq
from bisect import bisect_left, bisect_right


def solution(n, stages):
    rate = [0] * (n + 1)
    stages.sort()
    for i in range(1, n + 1):
        cnt = bisect_right(stages, i) - bisect_left(stages, i)
        length = len(stages) - bisect_left(stages, i)
        print(bisect_left(stages, i))
        print(length)
        rate[i] = cnt / length
    q = []
    for i in range(1, n + 1):
        heapq.heappush(q, (-rate[i], i))
    res = []
    while q:
        res.append(heapq.heappop(q)[1])
    return res


if __name__ == "__main__":
    n = 6
    stages = [2]
    print(solution(n, stages))
