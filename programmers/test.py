from collections import deque


def solution(n, t, m, table):
    timetable = [get_time(table[i]) for i in range(len(table))]
    shuttle_table = []
    shuttle_start = get_time("09:00")
    timetable.sort()
    que = deque(timetable)
    answer = 0
    for i in range(n):
        shuttle_table.append(shuttle_start)
        shuttle_start += t

    for i in range(len(shuttle_table)):
        arr = []
        for _ in range(m):
            if que and shuttle_table[i] >= que[0]:
                arr.append(que.popleft())
            else:
                break

        if i == len(shuttle_table) - 1:
            if len(arr) < m:
                answer = shuttle_table[i]
            else:
                answer = arr[-1] - 1

    return get_str_time(answer)


def get_time(time):
    hour = 60 * int(time[:2])
    minute = int(time[3:])
    return hour + minute


def get_str_time(time):
    hour = str(time // 60) if time // 60 >= 10 else "0" + str(time // 60)
    minute = str(time % 60) if time % 60 >= 10 else "0" + str(time % 60)
    return hour + ":" + minute


if __name__ == "__main__":
    n = 2
    t = 1
    m = 2
    table = ["09:00", "09:00", "09:00", "09:00"]
    print(solution(n, t, m, table))
