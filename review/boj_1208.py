# BOJ 1208
import sys

si = sys.stdin.readline


def dfs_left(idx, s):
    if idx == mid:
        left.append(s)
        return

    dfs_left(idx + 1, s + arr[idx])
    dfs_left(idx + 1, s)


def dfs_right(idx, s):
    if idx == n:
        right.append(s)
        return

    dfs_right(idx + 1, s + arr[idx])
    dfs_right(idx + 1, s)


def solve(left, right, target):
    cnt = 0
    lp = 0
    rp = len(right) - 1
    while lp < len(left) and rp >= 0:
        lv = left[lp]
        rv = right[rp]
        ret = lv + rv
        if ret == target:
            lc = 0
            rc = 0
            while lp < len(left) and lv == left[lp]:
                lc += 1
                lp += 1
            while rp >= 0 and rv == right[rp]:
                rc += 1
                rp -= 1
            cnt += lc * rc

        elif ret < target:
            lp += 1
        elif ret > target:
            rp -= 1

    if target == 0:
        cnt -= 1

    return cnt


left = []
right = []
n, m = map(int, si().split())
arr = list(map(int, si().split()))
mid = n // 2
dfs_left(0, 0)
dfs_right(mid, 0)
left.sort()
right.sort()
print(solve(left, right, m))