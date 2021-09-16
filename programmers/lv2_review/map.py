# [카카오] 비밀지도


def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        result.append((arr1[i] | arr2[i]))
    ret = []
    for i in range(n):
        string = ""
        for j in range(n):
            if result[i] & (1 << j):
                string = "#" + string
            else:
                string = " " + string
        ret.append(string)
    return ret


if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))