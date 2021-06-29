# [카카오] 광고 삽입
from collections import deque


def solution(play_time, adv_time, logs):
    vector = [0] * 360000
    que = deque()
    for log in logs:
        start_time = get_time(log[:8])
        end_time = get_time(log[9:])
        vector[start_time] += 1
        vector[end_time] -= 1

    length = get_time(adv_time)
    tot = get_time(play_time)
    max_idx = 0

    for i in range(1, len(vector)):
        vector[i] += vector[i - 1]

    s = 0
    for i in range(length):
        s += vector[i]
        que.append(vector[i])

    max_sum = s
    for i in range(length, tot):
        que.append(vector[i])
        s += vector[i]
        s -= que.popleft()
        if s > max_sum:
            max_sum = s
            max_idx = i - length + 1
    answer = get_str_time(max_idx)
    return answer


def get_time(time):
    hour = int(time[:2])
    minute = int(time[3:5])
    second = int(time[6:])
    return hour * 3600 + minute * 60 + second


def get_str_time(time):
    second = str(time % 60) if time % 60 >= 10 else "0" + str(time % 60)
    time //= 60
    minute = str(time % 60) if time % 60 >= 10 else "0" + str(time % 60)
    time //= 60
    hour = str(time) if time >= 10 else "0" + str(time)
    return hour + ":" + minute + ":" + second


if __name__ == "__main__":
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    print(solution(play_time, adv_time, logs))
