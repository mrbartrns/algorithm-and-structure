# 다리를 지나는 트럭
from collections import deque


def solution(bridge_length, weight, truck_weights):
    que = deque([0] * bridge_length)
    cur_weight = 0
    cnt = 0
    cars = deque(truck_weights)
    while que:
        v = que.popleft()
        cur_weight -= v
        if cars and cur_weight + cars[0] <= weight:
            car = cars.popleft()
            cur_weight += car
            que.append(car)
        elif cars and cur_weight + cars[0] > weight:
            que.append(0)
        cnt += 1
    return cnt


length = 100
weight = 100
truck = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution(length, weight, truck))