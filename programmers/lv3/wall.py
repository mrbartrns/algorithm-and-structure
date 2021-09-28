# [카카오] 외벽 점검
from bisect import bisect_right
from itertools import permutations

INF = 987654321


def solution(n, weak, dist):
    answer = INF
    size = len(weak)
    for i in range(size):
        weak.append(weak[i] + n)
    table = permutations(dist)
    for distance in table:
        for i in range(size):
            start = weak[i]
            end = weak[i + size - 1]
            for j in range(len(dist)):
                start += distance[j]
                if start >= end:
                    answer = min(answer, j + 1)
                    break
                else:
                    idx = bisect_right(weak, start)
                    start = weak[idx]
    return answer if answer < INF else -1


if __name__ == "__main__":
    n = 12
    weak = [1, 5, 6, 10]
    dist = [1, 2, 3, 4]
    print(solution(n, weak, dist))
