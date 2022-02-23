# BOJ 2616 소형 기관차
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def get_psum(arr):
    s = 0
    ret = [0]
    for i in range(len(arr)):
        s += arr[i]
        ret.append(s)
    return ret


N = int(si().strip())
arr = list(map(int, si().strip().split(" ")))
M = int(si().strip())
psum = get_psum(arr)
cache = [[0 for _ in range(len(psum))] for _ in range(4)]
for i in range(1, 4):
    for j in range(len(psum)):
        if j - M >= 0:
            cache[i][j] = max(cache[i][j], cache[i - 1][j - M] + psum[j] - psum[j - M])
        cache[i][j] = max(cache[i][j], cache[i][j - 1])
print(cache[3][N])
