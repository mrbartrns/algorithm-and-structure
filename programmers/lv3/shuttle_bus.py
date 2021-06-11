# 카카오 셔틀버스
from collections import deque


def solution(n, t, m, timetable):
    timetable.sort()
    shuttle_table = []
    time_table = deque()
    start_time = get_time("09", "00")

    # make time_table
    for c in timetable:
        hour = c[:2]
        minute = c[3:]
        time_table.append(get_time(hour, minute))

    # make shuttle table
    for _ in range(n):
        shuttle_table.append(start_time)
        start_time += t

    ans = solve(time_table, shuttle_table, m)
    return itos(ans)


def solve(time_table, shuttle_table, m):
    ret = 0
    for i in range(len(shuttle_table)):
        cnt = 0
        que = []
        while time_table and cnt < m:
            if time_table[0] > shuttle_table[i]:
                break
            que.append(time_table.popleft())
            cnt += 1
        if i == len(shuttle_table) - 1:
            if cnt == m:
                ret = que.pop() - 1
            else:
                ret = shuttle_table[i]
    return ret


def get_time(hour, minute):
    ret = int(minute)
    ret += int(hour) * 60
    return ret


def itos(time):
    minute = str(time % 60) if time % 60 >= 10 else "0" + str(time % 60)
    time //= 60
    hour = str(time) if time >= 10 else "0" + str(time)
    return f"{str(hour)}:{str(minute)}"


if __name__ == "__main__":
    n = 10
    t = 60
    m = 45
    timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                 "23:59", "23:59", "23:59", "23:59", "23:59"]
    print(solution(n, t, m, timetable))
