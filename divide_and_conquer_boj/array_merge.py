# BOJ 11728
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
arr_a = list(map(int, si().split()))
arr_b = list(map(int, si().split()))

# 두 배열을 더한 후 sort를 해도 괜찮음 > 이것도 합병의 하나의 방법!
def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res


sys.stdout.write(" ".join(list(map(str, merge(arr_a, arr_b)))))
