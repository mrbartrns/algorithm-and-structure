# [카카오] 외벽 점검
# 어떤 배열이 정렬되어 있을때, bisect 생각해내기
from bisect import bisect_right
from itertools import permutations

INF = 987654321


def solution(n, weak, dist):
    answer = INF
    size = len(weak)
    for i in range(size):
        weak.append(weak[i] + n)
    people = permutations(dist)
    for distance in people:
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
    weak = [1, 3, 4, 9, 10]
    dist = [3, 5, 7]
    print(solution(n, weak, dist))
