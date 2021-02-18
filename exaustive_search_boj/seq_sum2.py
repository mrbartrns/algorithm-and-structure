# BOJ 1208
import sys

si = sys.stdin.readline


def dfs_left(idx, s):
    if idx == half:
        l.append(s)
        return

    dfs_left(idx + 1, s + arr[idx])
    dfs_left(idx + 1, s)


def dfs_right(idx, s):
    if idx == n:
        r.append(s)
        return

    dfs_right(idx + 1, s + arr[idx])
    dfs_right(idx + 1, s)


n, t = map(int, si().split())
arr = list(map(int, si().split()))
half = n // 2
l = []
r = []
dfs_left(0, 0)
dfs_right(half, 0)
l.sort()
r.sort()
print(l, r)


def sort(l, r):
    l_idx = 0
    r_idx = len(r) - 1
    ans = 0
    while l_idx < len(l) and r_idx >= 0:
        lv = l[l_idx]
        rv = r[r_idx]

        if lv + rv == t:
            lc = 0
            rc = 0

            while l_idx < len(l) and l[l_idx] == lv:
                lc += 1
                l_idx += 1

            while r_idx >= 0 and r[r_idx] == rv:
                rc += 1
                r_idx -= 1

            ans += lc * rc

        # 이 조건을 쓰기 위해 투포인터가 필요한 것
        if lv + rv > t:
            r_idx -= 1

        if lv + rv < t:
            l_idx += 1

    if t == 0:
        ans -= 1

    return ans


print(sort(l, r))