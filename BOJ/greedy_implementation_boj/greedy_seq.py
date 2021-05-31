# BOJ 1744
import sys

si = sys.stdin.readline


n = int(si())
arr = []
for _ in range(n):
    arr.append(int(si()))
arr.sort(reverse=True)
# arr = [3, 3, 2, 1, 0, -1, -1, -2]
# arr = [3, 2, 1, -1]


def solve(arr):
    p_arr = []
    n_arr = []
    for i in range(len(arr)):
        if arr[i] > 0:
            p_arr.append(arr[i])
        else:
            n_arr.append(arr[i])
    n_arr.reverse()
    # print(n_arr)
    tot = 0

    # 오류 있음
    for i in range(0, len(p_arr), 2):
        ret = 0
        ret += p_arr[i]
        if i + 1 < len(p_arr):
            if p_arr[i + 1] > 1:
                ret *= p_arr[i + 1]
            else:
                ret += p_arr[i + 1]
        tot += ret

    for i in range(0, len(n_arr), 2):
        ret = 0
        ret += n_arr[i]
        if i + 1 < len(n_arr):
            ret *= n_arr[i + 1]
        tot += ret

    return tot


print(solve(arr))