# [카카오] 문자열 압축

INF = 987654321


def solution(s):
    if len(s) == 1:
        return 1

    ret = INF
    for jump in range(1, len(s) // 2 + 1):
        temp = []
        for i in range(0, len(s), jump):
            temp.append(s[i:i + jump])
        cnt = 1
        prev = temp[0]
        string = ""
        for i in range(1, len(temp)):
            if prev == temp[i]:
                cnt += 1
            else:
                string += prev if cnt == 1 else str(cnt) + prev
                prev = temp[i]
                cnt = 1
        string += prev if cnt == 1 else str(cnt) + prev
        ret = min(ret, len(string))
    return ret


if __name__ == "__main__":
    s = "a"
    print(solution(s))
