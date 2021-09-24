# [카카오] 무지의 먹방 라이브
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    s = 0
    last = 0
    length = len(q)
    while s + (q[0][0] - last) * length <= k:
        s += (q[0][0] - last) * length
        last = q[0][0]
        length -= 1
        heapq.heappop(q)

    # after excuted while, my index will be zero
    q.sort(key=lambda x: x[1])
    return q[(k - s) % length][1]


if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5
    print(solution(food_times, k))