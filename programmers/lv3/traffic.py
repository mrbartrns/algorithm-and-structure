# [카카오] 추석 트래픽
def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond


def get_start_time(time, duration):
    duration_time = int(1000 * float(duration[:-1]))
    return get_time(time) - duration_time + 1


def solution(lines):
    answer = 0
    end_time = []
    start_time = []
    for line in lines:
        _, t, dt = line.split(" ")
        et = get_time(t)
        st = get_start_time(t, dt)
        end_time.append(et)
        start_time.append(st)
    for i in range(len(lines)):
        cnt = 0
        for j in range(i, len(lines)):
            if start_time[j] - 1000 < end_time[i]:
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