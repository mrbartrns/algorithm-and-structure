# 셔틀 버스
from collections import deque


def solution(n, t, m, timetable):
    timetable.sort()
    shuttle_table = []
    time_table = deque()
    time = get_time("09:00")
    for _ in range(n):
        shuttle_table.append(time)
        time += t
    for i in range(len(timetable)):
        time_table.append(get_time(timetable[i]))
    ret = solve(m, shuttle_table, time_table)
    return get_str_time(ret)


def get_time(time):
    hour = int(time[:2])
    minute = int(time[3:])
    return 60 * hour + minute


def get_str_time(time):
    hour = str(time // 60) if time // 60 >= 10 else "0" + str(time // 60)
    minute = str(time % 60) if time % 60 >= 10 else "0" + str(time % 60)
    return hour + ":" + minute


def solve(m, shuttle_table, time_table):
    for i in range(len(shuttle_table)):
        q = []
        for _ in range(m):
            if time_table and time_table[0] <= shuttle_table[i]:
                q.append(time_table.popleft())
            else:
                break
        if i == len(shuttle_table) - 1:
            if len(q) == m:
                return q[-1] - 1
    return shuttle_table[-1]


if __name__ == "__main__":
    n = 10
    t = 60
    m = 45
    timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                 "23:59", "23:59", "23:59", "23:59", "23:59"]
    print(solution(n, t, m, timetable))
