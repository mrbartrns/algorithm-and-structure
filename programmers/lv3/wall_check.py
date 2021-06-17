# 외벽 점검
"""
그리디 형식으로 처음에 생각할 수 있으나 -> 문제의 입력 크기를 보고 완전 탐색으로도 해결이 가능함을 생각해 봐야 함
원형의 외벽을 표현하기 위해서는 나머지를 이용할 수도 있지만, 배열의 크기를 두배로 늘려서 이용할 수도 있다.
weak = [1, 5, 6, 10] -> weak = [1, 5, 6, 10, 13, 17, 18, 22] -> 이렇게 된다면 각 위치에 따라 연속된 K개의 정점을 방문 할 수
있는지의 여부를 파악하는 문제가 됨
어떤 친구에게 어느 벽의 청소를 맡길 것인지에 대한 사항 또한 고려해야 함
"""
from bisect import bisect_right
from itertools import permutations

INF = int(1e9)


def solution(n, weak, dist):
    answer = INF
    k = len(weak)
    for i in range(k):
        weak.append(weak[i] + n)
    # print(weak)
    dist_permutations = list(permutations(dist))
    for distance in dist_permutations:
        for i in range(k):
            start = weak[i]
            finish = weak[i + k - 1]
            for j in range(len(distance)):
                start += distance[j]
                if start >= finish:
                    answer = min(answer, j + 1)
                    break
                nxt = bisect_right(weak, start)
                start = weak[nxt]
    if answer == INF:
        return -1
    return answer


if __name__ == "__main__":
    n = 12
    weak = [1, 3, 4, 9, 10]
    dist = [3, 5, 7]
    print(solution(n, weak, dist))
