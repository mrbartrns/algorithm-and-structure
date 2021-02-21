# BOJ 1107
import sys

si = sys.stdin.readline


def solve(target):
    res = abs(target - 100)
    for i in range(1000001):
        str_i = str(i)
        flag = True
        for j in range(len(str_i)):
            if int(str_i[j]) in broken:
                flag = False
                break
        if flag:
            res = min(res, len(str_i) + abs(i - target))
    return res


target = int(si())
n = int(si())
broken = set(list(map(int, si().split())))


print(solve(target))
