import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    last_food = 0
    length = len(food_times)
    s = 0
    # 어떠한 값을 초과하는지 않는지 확인할 때에는 기준 값을 직접적으로 바꾸지 말고 또 다른 변수를 선언 할 것
    while s + (q[0][0] - last_food) * length <= k:
        s += (q[0][0] - last_food) * length
        last_food = heapq.heappop(q)[0]
        length -= 1

    q.sort(key=lambda x: x[1])
    return q[(k - s) % length][1]


if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5
    print(solution(food_times, k))