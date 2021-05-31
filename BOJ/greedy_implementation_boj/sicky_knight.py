# BOJ 1783
import sys

si = sys.stdin.readline


def solve(n, m):
    cnt = 1
    if n > 2 and m > 6:
        cnt += 4
        cnt += m - 7
        return cnt
    right = 1
    while cnt < 4 and right < m:
        if n > 2:
            right += 1
            cnt += 1
        elif n == 2:
            if right + 2 <= m:
                right += 2
                cnt += 1
            else:
                break
        else:
            break

    return cnt


n, m = map(int, si().split())
print(solve(n, m))
"""
n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m + 1) // 2))
else:
    if m <= 6:
        print(min(4, m))
    else:
        print(m - 2)
"""