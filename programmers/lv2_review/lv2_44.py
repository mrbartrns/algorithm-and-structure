# 예상 대진표
import math


def solution(n, a, b):
    if a > b:
        a, b = b, a
    start = 1
    end = n
    ans = int(math.log(n, 2))
    while start <= end:
        mid = (start + end) // 2
        if a <= mid and mid < b:
            return ans
        elif a <= mid and b <= mid:
            end = mid - 1
        elif a > mid and b > mid:
            start = mid + 1
        ans -= 1
    return ans


n = 2 ** 20
a = 1
b = 2
print(solution(n, a, b))