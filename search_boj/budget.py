# BOJ 2512
import sys

"""
접근 방식
1. 예산의 중간값을 정하기
2. 중간값을 이용하여 배열을 순회하면서 중간값보다 작으면 그 값을 그대로 더하고, 중간값보다 크다면 중간값을 더한다.
3. 그 합이 전체 예산보다 크다면, 중간값을 낮추고, 작거나 같다면 중간값을 높인다.
"""
si = sys.stdin.readline


def get_value(qu, limit):
    size = len(qu)
    s = 0
    for i in range(size):
        if qu[i] < limit:
            s += qu[i]
        else:
            s += limit
    return s


def solve(req, value):
    start = 0
    end = req[-1]  # end scope is not to budget else req[-1]   return s
    ret = 0
    while start <= end:
        limit = (start + end) // 2
        s = get_value(req, limit)
        if s <= value:
            ret = limit
            start = limit + 1
        else:
            end = limit - 1
    return ret


n = int(si())
requests = list(map(int, si().split()))
budget = int(si())
requests.sort()

print(solve(requests, budget))
