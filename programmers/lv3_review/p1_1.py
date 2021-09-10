# [카카오] 추석 트래픽


def get_end_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond


def get_start_time(time, duration_time):
    int_duration_time = int(float(duration_time[:-1]) * 1000)
    return get_end_time(time) - int_duration_time + 1


def solution(lines):
    start = []
    end = []
    for line in lines:
        _, time, duration_time = line.split(" ")
        start.append(get_start_time(time, duration_time))
        end.append(get_end_time(time))
    answer = 0
    for i in range(len(lines)):
        cnt = 0
        for j in range(i, len(lines)):
            if end[i] + 1000 > start[j]:
                cnt += 1
        answer = max(answer, cnt)
    return answer


if __name__ == "__main__":
    lines = [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s",
    ]
    print(solution(lines))