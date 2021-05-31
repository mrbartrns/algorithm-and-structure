# BOJ 1041
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
INF = 250000000000000


def get_sum3(v):
    temp = [0, 1, 5, 4]
    temp2 = [1, 5, 4, 0]
    res = v[0] + v[1] + v[2]
    for i in range(4):
        if v[temp[i]] + v[temp2[i]] + v[3] > v[temp[i]] + v[temp2[i]] + v[2]:
            res = min(res, v[temp[i]] + v[temp2[i]] + v[2])
        else:
            res = min(res, v[temp[i]] + v[temp2[i]] + v[3])
    return res


def get_sum2(v):
    res = v[0] + v[1]
    for i in range(6):
        for j in range(i + 1, 6):
            if (i == 0 and j == 5) or (i == 1 and j == 4) or (i == 2 and j == 3):
                continue
            res = min(res, v[i] + v[j])
    return res


s3 = get_sum3(arr)
s2 = get_sum2(arr)
arr.sort()
res = 0
if n >= 2:
    res += 4 * s3
    res += 2 * (n - 3) * s2
    res += arr[0] * (n - 2) * (n - 2)
    res += arr[0] * (n - 2) * (n - 1) * 4
    print(res)
else:
    print(sum(arr) - arr[-1])
