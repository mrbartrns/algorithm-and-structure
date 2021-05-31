# BOJ 2143
import sys

si = sys.stdin.readline

# 부배열 만들기
t = int(si())
n = int(si())
arr_a = list(map(int, si().split()))
m = int(si())
arr_b = list(map(int, si().split()))
left = []
right = []

for i in range(n):
    s = 0
    for j in range(n):
        if i + j >= n:
            break
        else:
            s += arr_a[i + j]
            left.append(s)

for i in range(m):
    s = 0
    for j in range(m):
        if i + j >= m:
            break
        else:
            s += arr_b[i + j]
            right.append(s)

left.sort()
right.sort()


ans = 0
lp = 0
rp = len(right) - 1
while lp < len(left) and rp >= 0:
    lv = left[lp]
    rv = right[rp]
    ret = lv + rv
    if ret == t:
        lc = 0
        rc = 0
        while lp < len(left) and lv == left[lp]:
            lc += 1
            lp += 1
        while rp >= 0 and rv == right[rp]:
            rc += 1
            rp -= 1

        ans += lc * rc
    elif ret > t:
        rp -= 1
    elif ret < t:
        lp += 1

sys.stdout.write(str(ans))