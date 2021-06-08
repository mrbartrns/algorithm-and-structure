def solution(play_time, adv_time, logs):
    vector = [0] * 360000
    for log in logs:
        start_time = get_time(log[:8])
        end_time = get_time(log[9:])
        for i in range(start_time, end_time):
            vector[i] += 1

    length = get_time(adv_time)
    tot = get_time(play_time)
    max_idx = 0
    s = 0
    for i in range(length):
        s += vector[i]

    max_sum = s
    left = 0
    right = length - 1
    while right < tot:
        s -= vector[left]
        left += 1
        right += 1
        s += vector[right]
        if max_sum < s:
            max_sum = s
            max_idx = left
    answer = get_string_time(max_idx)
    return answer


def get_time(time):
    h = time[:2]
    m = time[3:5]
    s = time[6:]
    ret = 3600 * int(h) + 60 * int(m) + int(s)
    return ret


def get_string_time(time):
    s = str(time % 60) if time % 60 >= 10 else "0" + str(time % 60)
    time //= 60
    m = time % 60 if time % 60 >= 10 else "0" + str(time % 60)
    time //= 60
    h = time if time >= 10 else "0" + str(time % 60)
    return f"{h}:{m}:{s}"


if __name__ == "__main__":
    play_time = "99:59:59"
    adv_time = "25:00:00"
    logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    print(solution(play_time, adv_time, logs))
