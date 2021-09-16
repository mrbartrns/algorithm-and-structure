# [카카오] 캐시


def solution(cache_size, cities):
    answer = 0
    cache = []
    s = set()
    for i in range(len(cities)):
        city = cities[i].lower()
        if city not in s:
            answer += 5
            s.add(city)
            cache.append(city)
            if len(cache) > cache_size:
                prev = cache.pop(0)
                s.remove(prev)
        else:
            answer += 1
            for idx in range(cache_size):
                if cache[idx] == city:
                    cache.pop(idx)
                    cache.append(city)
                    break
    return answer


if __name__ == "__main__":
    cache_size = 0
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(
        solution(
            cache_size,
            cities,
        )
    )
