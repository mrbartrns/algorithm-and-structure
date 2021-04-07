# BOJ 13335
import sys
from collections import deque

si = sys.stdin.readline

n, length, maximum_weight = map(int, si().split())
trucks = deque(list(map(int, si().split())))
cur_weight = 0
time = 0
que = deque([0] * length)
while que:
    cur_weight -= que.popleft()
    if trucks and cur_weight + trucks[0] <= maximum_weight:
        truck = trucks.popleft()
        que.append(truck)
        cur_weight += truck
    elif trucks:
        que.append(0)
    time += 1

print(time)
