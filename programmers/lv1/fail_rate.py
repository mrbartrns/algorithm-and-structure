# [카카오] 실패율
import heapq


def solution(n, stages):
    answer = []
    counts = [0] * (n + 1)
    length = len(stages)
    q = []

    for i in stages:
        if i < n + 1:
            counts[i] += 1

    for i in range(1, n + 1):
        if length > 0:
            rate = counts[i] / length
            heapq.heappush(q, (-rate, i))
            length -= counts[i]
        else:
            heapq.heappush(q, (0, i))

    while q:
        _, i = heapq.heappop(q)
        answer.append(i)
    return answer


if __name__ == "__main__":
    n = 5
    stages = [4, 4, 4, 4, 4]
    print(solution(n, stages))