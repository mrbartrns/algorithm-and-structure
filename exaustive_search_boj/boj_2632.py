# BOJ 2632
import sys

si = sys.stdin.readline


def add(arr, t):
    psum = [0] * 2000001
    psum[0] = 1  # 아무것도 더하지 않는 경우의 수
    for i in range(len(arr)):
        s = 0
        for j in range(len(arr)):
            s += arr[(i + j) % len(arr)]
            if s > t:
                break
            else:
                psum[s] += 1
    psum[sum(arr)] = 1
    return psum


def solve(left, right, t):
    res = 0
    for i in range(t + 1):
        res += left[i] * right[t - i]
    return res


t = int(si())
n, m = map(int, si().split())
left = [int(si()) for _ in range(n)]
right = [int(si()) for _ in range(m)]

lsum = add(left, t)
rsum = add(right, t)

print(solve(lsum, rsum, t))