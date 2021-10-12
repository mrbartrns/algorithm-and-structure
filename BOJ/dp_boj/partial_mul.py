# BOJ 2670 연속 부분 최대곱
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def get_partial_mul(arr):
    ret = [arr[i] for i in range(N)]
    for i in range(1, N):
        ret[i] = max(ret[i], ret[i] * ret[i - 1])
    return ret


N = int(si())
arr = [float(si()) for _ in range(N)]

dp = get_partial_mul(arr)
print("%.3f" % max(dp))
