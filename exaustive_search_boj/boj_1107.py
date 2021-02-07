# BOJ 1107
import sys

si = sys.stdin.readline

n = int(si())
m = int(si())
broken = set(si().split())  # O(1)으로 탐색하기 위한 해시구조 만들기 (string)


def solve(n, broken):
    cnt = abs(100 - n)
    for i in range(1000001):
        str_i = str(i)
        flag = True
        for j in range(len(str_i)):
            if str_i[j] in broken:
                flag = False
                break
        if flag:
            cnt = min(cnt, abs(i - n) + len(str_i))
    return cnt


print(solve(n, broken))