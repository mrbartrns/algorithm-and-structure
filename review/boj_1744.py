# BOJ 1744
import sys

si = sys.stdin.readline


def solve(p, n):
    cnt = 0
    for i in range(0, len(p), 2):
        ps = p[i]
        if i + 1 < len(p) and p[i + 1] > 1:
            ps *= p[i + 1]
        elif i + 1 < len(p) and p[i + 1] <= 1:
            ps += p[i + 1]
        cnt += ps

    for i in range(0, len(n), 2):
        ns = n[i]
        if i + 1 < len(n):
            ns *= n[i + 1]
        cnt += ns
    return cnt


n = int(si())
p_, n_ = [], []

for _ in range(n):
    num = int(si())
    if num > 0:
        p_.append(num)
    else:
        n_.append(num)

p_.sort(reverse=True)
n_.sort()
print(solve(p_, n_))
