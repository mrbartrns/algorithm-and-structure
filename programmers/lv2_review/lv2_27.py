# 튜플
from bisect import bisect_left, bisect_right


def solution(s):
    check = set()
    exception = set(["{", "}", ","])
    arr = []
    temp = ""
    for i in range(len(s)):
        if s[i] not in exception:
            temp += s[i]
        elif temp:
            if int(temp) not in check:
                check.add(int(temp))
            arr.append(int(temp))
            temp = ""
    arr.sort()
    ans = [i for i in check]
    ans.sort(key=lambda x: -(bisect_right(arr, x) - bisect_left(arr, x)))
    return ans


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))