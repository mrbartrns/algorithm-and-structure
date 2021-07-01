# 외벽 점검
"""
레스토랑의 구조는 완전히 동그란 모양이고 -> 경계선이 없다
좌로 우로 이동할 수 있고, 그 결과가 같기때문에 한쪽 방향으로만 이동할 수 있다고 가정
따라서 배열의 크기를 두배 늘리고, 배열의 각 요소에 n만큼 더한 값을 넣어주면 배열의 범위 내에서 해결할 수 있게 됨
Examples:
    n = 12, weak = [1, 5, 6, 10], dist = [1, 2, 3, 4]
    weak = [1, 5, 6, 10, 13, 17, 18, 22]
친구가 각 시간을 통해 이동할 수 있는 거리가 주어지고, 출발하는 위치는 어디에서 출발하던지 상관 없다.
친구들의 순서를 permutations를 통해 결정하고, weakpoint의 어느 위치부터 출발할 것인지 결정을 해주면된다.
permutaions 하기만 하면 되고, 백트래킹은 따로 할 필요가 없다.
"""
from bisect import bisect_right
from itertools import permutations

INF = 987654321


def solution(n, weak, dist):
    size = len(weak)
    answer = INF
    for i in range(size):
        weak.append(n + weak[i])
    dist_permutations = permutations(dist)
    for distance in dist_permutations:
        for i in range(size):
            start = weak[i]
            finish = weak[i + size - 1]
            for j in range(len(distance)):
                start += distance[j]
                if start >= finish:
                    answer = min(answer, j + 1)
                    break
                nxt = bisect_right(weak, start)
                start = weak[nxt]
    return answer if answer < INF else -1


if __name__ == "__main__":
    n = 12
    weak = [1, 3, 4, 9, 10]
    dist = [3, 5, 7]
    print(solution(n, weak, dist))
