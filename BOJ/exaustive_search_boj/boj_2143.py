# BOJ 2143
import sys

si = sys.stdin.readline


def add(arr):
    psum = []
    for i in range(len(arr)):
        s = 0
        for j in range(len(arr)):
            if i + j >= len(arr):
                break
            s += arr[i + j]
            psum.append(s)
    psum.sort()
    return psum


def solve(left, right, t):
    lp = 0
    rp = len(right) - 1
    res = 0
    while lp < len(left) and rp >= 0:
        lv = left[lp]
        rv = right[rp]
        ret = lv + rv
        if ret == t:
            lc = rc = 0
            while lp < len(left) and left[lp] == lv:
                lc += 1
                lp += 1

            while rp >= 0 and right[rp] == rv:
                rc += 1
                rp -= 1

            res += lc * rc

        elif ret > t:
            rp -= 1

        else:
            lp += 1

    return res


t = int(si())
n = int(si())
left = list(map(int, si().split()))
m = int(si())
right = list(map(int, si().split()))
lsum = add(left)
rsum = add(right)
print(solve(lsum, rsum, t))