# BOJ 7453
import sys

si = sys.stdin.readline

n = int(si())
a, b, c, d = [], [], [], []
for _ in range(n):
    w, x, y, z = map(int, si().split())
    a.append(w)
    b.append(x)
    c.append(y)
    d.append(z)


def add(a, b):
    arr = []
    for i in range(n):
        for j in range(n):
            arr.append(a[i] + b[j])
    arr.sort()
    return arr


def solve(left, right):
    res = lp = 0
    rp = len(right) - 1
    while lp < len(left) and rp >= 0:
        lv = left[lp]
        rv = right[rp]
        ret = lv + rv
        if ret == 0:
            lc = rc = 0
            while lp < len(left) and left[lp] == lv:
                lc += 1
                lp += 1

            while rp >= 0 and right[rp] == rv:
                rc += 1
                rp -= 1

            res += lc * rc
        elif ret > 0:
            rp -= 1
        else:
            lp += 1
    return res


left = add(a, b)
right = add(c, d)

print(solve(left, right))