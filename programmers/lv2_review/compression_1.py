# [카카오] 문자열 압축

INF = 987654321


def solution(s):
    if len(s) <= 1:
        return 1
    answer = INF
    for jump in range(1, len(s) // 2 + 1):
        ret = ""
        substring = s[0:jump]
        cnt = 0
        for i in range(0, len(s), jump):
            j = i + jump
            if substring != s[i:j]:
                ret += substring if cnt < 2 else str(cnt) + substring
                substring = s[i:j]
                cnt = 1
            else:
                cnt += 1
        ret += substring if cnt < 2 else str(cnt) + substring
        answer = min(answer, len(ret))
    return answer


if __name__ == "__main__":
    s = "a"
    print(solution(s))