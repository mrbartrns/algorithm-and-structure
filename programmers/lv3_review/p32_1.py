# [카카오] 외벽 점검
from itertools import permutations
from bisect import bisect_right


INF = 987654321


def solution(n, weak, dist):
    answer = INF
    size = len(weak)
    for i in range(size):
        weak.append(weak[i] + n)
    distance_set = permutations(dist)
    for distance in distance_set:
        for i in range(size):
            start = weak[i]
            end = weak[i + size - 1]
            for j in range(len(distance)):
                start += distance[j]
                if start >= end:
                    answer = min(answer, j + 1)
                else:
                    idx = bisect_right(weak, start)
                    start = weak[idx]
    return answer if answer < INF else -1


if __name__ == "__main__":
    n = 12
    weak = [1, 5, 6, 10]
    dist = [1, 2, 3, 4]
    print(solution(n, weak, dist))