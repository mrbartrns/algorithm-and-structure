# 야근 지수
import heapq
from functools import reduce


def solution(n, works):
    q = list(map(lambda x: -x, works))
    heapq.heapify(q)

    for i in range(n):
        if q:
            num = heapq.heappop(q)
            num += 1
            if num < 0:
                heapq.heappush(q, num)

    answer = reduce(lambda acc, cur: acc + cur ** 2, q, 0)
    return answer


if __name__ == "__main__":
    works = [1, 1]
    n = 3
    print(solution(n, works))
