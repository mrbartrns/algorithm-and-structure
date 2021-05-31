# BOJ 7453
import sys

si = sys.stdin.readline

n = int(si())
a_arr, b_arr, c_arr, d_arr = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, si().split())
    a_arr.append(a)
    b_arr.append(b)
    c_arr.append(c)
    d_arr.append(d)

a_b_sum = []
c_d_sum = []
for i in range(n):
    for j in range(n):
        a_b_sum.append(a_arr[i] + b_arr[j])
        c_d_sum.append(c_arr[i] + d_arr[j])

a_b_sum.sort()
c_d_sum.sort()

# 투 포인터
lp = 0
rp = len(c_d_sum) - 1
ans = 0
while lp < len(a_b_sum) and rp >= 0:
    lv = a_b_sum[lp]
    rv = c_d_sum[rp]
    ret = lv + rv
    if ret == 0:
        lc = 0
        rc = 0
        while lp < len(a_b_sum) and a_b_sum[lp] == lv:
            lp += 1
            lc += 1

        while rp >= 0 and c_d_sum[rp] == rv:
            rp -= 1
            rc += 1

        ans += lc * rc

    elif ret > 0:
        rp -= 1
    elif ret < 0:
        lp += 1

print(ans)
