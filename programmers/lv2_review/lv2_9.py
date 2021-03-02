# 카카오 문자열 압축
def solution(s):
    MAX = 10000
    ans = MAX
    for i in range(1, len(s) + 1):
        new_string = solve(s, i)
        ans = min(ans, len(new_string))
    return ans


def solve(string, k):
    last = string[0:k]
    cnt = 1
    new_string = ""
    for i in range(k, len(string), k):
        cur = string[i : i + k]
        if last == cur:
            cnt += 1
        else:
            if cnt > 1:
                new_string += str(cnt) + last
            else:
                new_string += last
            last = cur
            cnt = 1

    if cnt > 1:
        new_string += str(cnt) + last
    else:
        new_string += last

    return new_string


print(solution("xababcdcdababcdcd"))
