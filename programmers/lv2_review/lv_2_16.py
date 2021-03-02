# 더 맵게
import heapq


def solution(q, K):
    cnt = 0
    heapq.heapify(q)
    while q:
        mini = heapq.heappop(q)
        if mini >= K:
            return cnt
        if q:
            cnt += 1
            min_next = heapq.heappop(q)
            new_ = mini + min_next * 2
            heapq.heappush(q, new_)
    return -1


scoville = [0, 0, 3, 9, 10, 12]
K = 0
print(solution(scoville, K))