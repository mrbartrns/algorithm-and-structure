# [카카오] 방금 그곡


def make_process(song):
    stack = []
    prev = ""
    for c in song:
        if c == "#":
            stack.pop()
            if prev == "C":
                stack.append("H")
            elif prev == "D":
                stack.append("I")
            elif prev == "F":
                stack.append("J")
            elif prev == "G":
                stack.append("K")
            elif prev == "A":
                stack.append("L")
        else:
            stack.append(c)
        prev = c
    return "".join(stack)


def get_time(time):
    hour = int(time[:2]) * 60
    minute = int(time[3:])
    return hour + minute


def solution(m, musicinfos):
    music_table = []
    for i in range(len(musicinfos)):
        st, et, title, info = musicinfos[i].split(",")
        t = get_time(et) - get_time(st)
        music = make_process(info)
        length = len(music)
        sheet = []
        for i in range(t):
            sheet.append(music[i % length])
        music_table.append(("".join(sheet), st, title))
    my_music = make_process(m)
    music_table.sort(key=lambda x: (-len(x[0]), x[1]))
    for i in range(len(music_table)):
        if my_music in music_table[i][0]:
            return music_table[i][2]
    return "(None)"


if __name__ == "__main__":
    m = "ABCDEFG"
    musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    # print(make_process("ABC#D#EF#G#"))
    print(solution(m, musicinfos))
