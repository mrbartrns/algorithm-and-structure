# BOJ 1208
import sys

si = sys.stdin.readline


def dfs_left(idx, s):
    if idx == half:
        left.append(s)
        return

    dfs_left(idx + 1, s)
    dfs_left(idx + 1, s + arr[idx])


def dfs_right(idx, s):
    if idx == n:
        right.append(s)
        return

    dfs_right(idx + 1, s)
    dfs_right(idx + 1, s + arr[idx])


n, s = map(int, si().split())
arr = list(map(int, si().split()))
half = n // 2
left, right = [], []
dfs_left(0, 0)
dfs_right(half, 0)
left.sort()
right.sort()


lp = 0
rp = len(right) - 1
ans = 0
while (lp < len(left)) and (rp >= 0):
    lv = left[lp]
    rv = right[rp]
    ret = lv + rv
    if ret < s:
        lp += 1
    elif ret > s:
        rp -= 1
    else:
        lc, rc = 0, 0
        while (lp < len(left)) and (left[lp] == lv):
            lc += 1
            lp += 1

        while (rp >= 0) and (right[rp] == rv):
            rc += 1
            rp -= 1

        ans += lc * rc

if s == 0:
    ans -= 1

print(ans)