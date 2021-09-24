# [카카오] 광고 삽입
from collections import deque


def get_str_time(time):
    second = str(time % 60) if time % 60 >= 10 else "0" + str(time % 60)
    time //= 60
    minute = str(time % 60) if time % 60 >= 10 else "0" + str(time % 60)
    time //= 60
    hour = str(time) if time >= 10 else "0" + str(time)
    return hour + ":" + minute + ":" + second


def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:])
    return hour + minute + second


def solution(play_time, adv_time, logs):
    timeline = [0] * 360000
    for log in logs:
        st, et = log.split("-")
        start_time, end_time = get_time(st), get_time(et)
        timeline[start_time] += 1
        timeline[end_time] -= 1
    for i in range(1, len(timeline)):
        timeline[i] += timeline[i - 1]

    que = deque()
    ad_time = get_time(adv_time)
    tot = get_time(play_time)
    s = 0
    for i in range(ad_time):
        que.append(timeline[i])
        s += timeline[i]
    max_value = s
    answer = 0
    for i in range(ad_time, tot):
        s -= que.popleft()
        s += timeline[i]
        que.append(timeline[i])
        if max_value < s:
            max_value = s
            answer = i - ad_time + 1
    return get_str_time(answer)


if __name__ == "__main__":
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs = [
        "01:20:15-01:45:14",
        "00:40:31-01:00:00",
        "00:25:50-00:48:29",
        "01:30:59-01:53:29",
        "01:37:44-02:02:30",
    ]
    print(solution(play_time, adv_time, logs))