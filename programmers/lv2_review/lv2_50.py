# 방금 그곡
def solution(m, musicinfos):
    ans = "(None)"
    l_time = 0
    for info in musicinfos:
        arr = info.split(",")
        s_time = list(arr[0].split(":"))
        e_time = list(arr[1].split(":"))
        s_hour, s_min = int(s_time[0]), int(s_time[1])
        e_hour, e_min = int(e_time[0]), int(e_time[1])
        time = (e_hour - s_hour) * 60 + (e_min - s_min)

        music_info = arr[3]
        string = solve(music_info, time)
        print(string)

        if check(m, string) and l_time < time:
            ans = arr[2]
            l_time = time

    return ans


def check(m, info):
    size = len(m)
    for i in range(len(info)):
        if i + size >= len(info) or info[i + size] == "#":
            continue
        if m == info[i : size + i]:
            return True
    return False


def solve(info, time):
    i = 0  # time
    j = 0  # idx
    new_ = ""
    while True:
        if i >= time:
            break
        c = info[j % len(info)]
        new_ += c
        if c != "#":
            i += 1
        j += 1
    return new_


m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
