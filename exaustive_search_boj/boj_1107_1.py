# BOJ 1107
import sys

si = sys.stdin.readline

n = int(si())
m = int(si())
broken_btns = set(si().split())


def solve(n, btns):
    res = abs(n - 100)
    for i in range(1000001):
        str_i = str(i)
        flag = True
        for j in range(len(str_i)):
            if str_i[j] in btns:
                flag = False
                break
        if flag:
            res = min(res, abs(n - i) + len(str_i))
    return res


print(solve(n, broken_btns))