# [카카오] 무지의 먹방 라이브
"""
힙 큐를 이용하면 매우매우 간단하게 풀 수 있음 -> 인덱스 저장 필요
"""
import heapq


def solution(food_times, k):
    # 안되는 조건이 언제인지 생각해보고 미리 빼놓기
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i))

    # 먹기 위해 사용한 시간
    s = 0
    # 직전에 다 먹은 시간
    prev = 0
    # 남은 음식의 갯수
    length = len(food_times)

    while s + (q[0][0] - prev) * length <= k:
        idx = heapq.heappop(q)[0]
        s += (idx - prev) * length
        length -= 1
        prev = idx
    result = sorted(q, key=lambda x: x[1])
    return result[(k - s) % length][1] + 1


if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 1
    print(solution(food_times, k))
