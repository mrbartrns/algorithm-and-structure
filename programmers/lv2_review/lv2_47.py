# 캐시
from collections import deque

"""
--------------------------->
이전                     최신

"""


def solution(cache_size, cities):
    cache = deque()
    cnt = 0
    cities = list(map(lambda x: x.lower(), cities))

    if cache_size > 0:
        for i in range(len(cities)):
            if cities[i] not in cache:
                if len(cache) == cache_size:
                    cache.popleft()
                cache.append(cities[i])
                cnt += 5
            else:
                temp = []
                idx = 0
                for j in range(len(cache)):
                    if cache[j] == cities[i]:
                        idx = j

                for _ in range(idx):
                    temp.append(cache.popleft())

                cache.append(cache.popleft())

                size = len(temp)
                for _ in range(size):
                    cache.appendleft(temp.pop())
                cnt += 1
    else:
        return len(cities) * 5
    return cnt


size = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(size, cities))