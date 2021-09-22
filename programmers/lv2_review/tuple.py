# [카카오] 튜풀
from bisect import bisect_left, bisect_right


def solution(s):
    digit = []
    arr = s[2:-2].split("},{")
    for i in range(len(arr)):
        arr[i] = arr[i].split(",")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            digit.append(int(arr[i][j]))
    digit.sort()
    answer = [i for i in set(digit)]
    answer.sort(key=lambda x: -(bisect_right(digit, x) - bisect_left(digit, x)))
    return answer


if __name__ == "__main__":
    s = "{{20,111},{111}}"
    print(solution(s))