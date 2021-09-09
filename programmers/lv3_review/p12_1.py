# [카카오] 셔틀버스
from collections import deque


def get_str_time(time):
    minute = str(time % 60) if time % 60 >= 10 else "0" + str(time % 60)
    hour = str(time // 60) if time // 60 >= 10 else "0" + str(time // 60)
    return hour + ":" + minute


def get_time(time):
    hour = int(time[:2])
    minute = int(time[3:])
    return hour * 60 + minute


def solution(n, t, m, time_table):
    start_time = get_time("09:00")
    bus_table = []

    for _ in range(n):
        bus_table.append(start_time)
        start_time += t
    temp = []
    for t in time_table:
        temp.append(get_time(t))

    temp.sort()
    que = deque(temp)

    for i in range(n):
        bus = []
        while que:
            if que[0] <= bus_table[i]:
                bus.append(que.popleft())
            else:
                break
            if len(bus) >= m:
                break
        if i == n - 1:
            if len(bus) == m:
                return get_str_time(bus[-1] - 1)
            else:
                return get_str_time(bus_table[n - 1])


if __name__ == "__main__":
    n = 2
    t = 10
    m = 2
    time_table = ["09:10", "09:09", "08:00"]
    print(solution(n, t, m, time_table))
