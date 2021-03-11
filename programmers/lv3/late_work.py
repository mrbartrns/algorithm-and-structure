# 야근 지수
# 그리디로 해결할 수 있는 이유 및 다른방법이 있는지 탐색하기
import heapq as hq
from functools import reduce


def solution(n, works):
    q = []
    for i in range(len(works)):
        hq.heappush(q, -works[i])
    for _ in range(n):
        if q:
            u = hq.heappop(q)
            u = -u
            if u > 0:
                u -= 1
                hq.heappush(q, -u)
    value = reduce(lambda acc, cur: acc + cur ** 2, q, 0)
    return value


def solve(acc, cur):
    acc += cur ** 2
    return acc


works = [1, 1]
n = 3
print(solution(n, works))