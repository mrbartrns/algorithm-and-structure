# BOJ 7453
import sys

si = sys.stdin.readline
n = int(si())
l, r = map(int, si().split())
l_temp = [int(si()) for _ in range(l)]
r_temp = [int(si()) for _ in range(r)]


def add(a, target, arr):
    res = [0] * 2000001
    res[0] = 1
    for i in range(a):
        s = 0
        for j in range(a):
            s += arr[(i + j) % a]
            if s > target:
                break
            else:
                res[s] += 1
    res[sum(arr)] = 1
    return res


def solve(left, right, target):
    res = 0
    for i in range(target + 1):
        res += left[i] * right[target - i]
    return res


left = add(l, n, l_temp)
right = add(r, n, r_temp)
print(solve(left, right, n))