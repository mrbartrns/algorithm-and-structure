# 이진 변환 반복하기
def solution(s):
    ans = [0, 0]
    string = s
    while string != "1":
        new_string = ""
        for i in range(len(string)):
            if string[i] == "0":
                ans[1] += 1
            else:
                new_string += string[i]

        n = len(new_string)
        string = get_bin(n)
        ans[0] += 1
    return ans


def get_bin(n):
    res = ""
    if n == 0:
        return res

    if n % 2 == 0:
        res = get_bin(n // 2) + "0"
    else:
        res = get_bin(n // 2) + "1"
    return res


print(solution("1111111"))