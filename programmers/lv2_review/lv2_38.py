# JadenCase 문자열 만들기
a = "b c d"


def solution(s):
    arr = s.split(" ")
    for k in range(len(arr)):
        new_ = ""
        for i in range(len(arr[k])):
            if i == 0:
                if ord("a") <= ord(arr[k][i]) and ord(arr[k][i]) <= ord("z"):
                    new_ += chr(ord(arr[k][i]) - (ord("a") - ord("A")))
                else:
                    new_ += arr[k][i]
            else:
                if ord("A") <= ord(arr[k][i]) and ord(arr[k][i]) <= ord("Z"):
                    new_ += chr(ord(arr[k][i]) + (ord("a") - ord("A")))
                else:
                    new_ += arr[k][i]
        arr[k] = new_
    return " ".join(arr)


print(solution("3people unFollowed me"))
