# 합친 LIS
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


# 완전탐색으로 해결하기
def jlis(a, b, p):
    if a > A:
        return 0
    if b > B:
        return 0

    ret = 0
    for i in range(a + 1, A):
        if not p or p[-1] < arr1[i]:
            ret = max(ret, 1 + jlis(i, b, p[:] + [arr1[i]]))
    for j in range(b + 1, B):
        if not p or p[-1] < arr2[j]:
            ret = max(ret, 1 + jlis(a, j, p[:] + [arr2[j]]))
    return ret


T = int(si())
for _ in range(T):
    A, B = map(int, si().split(" "))
    arr1 = list(map(int, si().split(" ")))
    arr2 = list(map(int, si().split(" ")))
    print(jlis(-1, -1, []))
