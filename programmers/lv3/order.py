# 줄 서는 방법
"""
1234
1243
1324
1342
1423
1432
"""
from itertools import permutations


def solution(n, k):
    arr = [i for i in range(1, n + 1)]
    hash_set = set(arr)
    ret = get_arr(n, k - 1, arr, hash_set)
    return ret


def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)


def get_arr(n, k, arr, hash_set):
    ans = []
    if n == 0:
        return ans
    idx = k // factorial(n - 1)
    left = k % factorial(n - 1)
    cnt = 0
    chk = 0
    while True:
        if arr[cnt] in hash_set:
            if chk == idx:
                hash_set.remove(arr[cnt])
                ans = [arr[cnt]] + get_arr(n - 1, left, arr, hash_set)
                break
            chk += 1
        cnt += 1
    return ans


if __name__ == "__main__":
    n = 3
    k = 6
    print(solution(n, k))
    # print(factorial(n - 1))
