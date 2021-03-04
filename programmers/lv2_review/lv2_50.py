def solution(m, musicinfos):
    ans = "(None)"
    longest = 0
    for i in range(len(musicinfos)):
        arr = list(musicinfos[i].split(","))

        title = arr[2]
        music_info = arr[3]

        # 시간 설정하기
        # 4, 11번 틀린 이유 -> 끝나는시간을 24로 조정하면서 문제가 있었음
        s = list(arr[0].split(":"))
        e = list(arr[1].split(":"))
        s_hour, s_minutes = int(s[0]), int(s[1])
        e_hour = int(e[0])
        e_minutes = int(e[1])

        # 시간 반환
        time = 60 * (e_hour - s_hour) + (e_minutes - s_minutes)

        new_string = solve(time, music_info)

        if check(m, new_string) and longest < time:
            ans = title
            longest = time

    return ans


def check(m, info):
    # m의 길이만큼 순회하면서 확인해보기
    # ABC가 일치하지만 마지막 글자 뒤에 #이 있다면 체크하지 않는다
    # EE# 같은 경우에 대해서도 체크
    size = len(m)
    idx = info.find(m)
    while idx > -1:
        if idx + size < len(info) and info[idx + size] == "#":
            idx = info.find(m, idx + size)
        else:
            return True
    return False


def solve(time, info):
    cur_time, cur_idx = 0, 0
    size = len(info)
    new_string = ""
    while True:
        c = info[cur_idx % size]
        if cur_time == time:
            if c == "#":
                new_string += c
            break
        if c != "#":
            cur_time += 1
        new_string += c
        cur_idx += 1
    return new_string


m = "CDCDF"
string = "CDCDCDF"
print(check(m, string))