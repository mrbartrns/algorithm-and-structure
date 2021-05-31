# BOJ 2089
import sys

input = sys.stdin.readline


def solve_iter(n):
    copy = n
    res = ""
    while copy != 0:
        if copy % -2 == 0:
            res = "0" + res
            copy = copy // -2
        else:
            res = "1" + res
            copy = copy // -2 + 1
    return res


n = int(input())
print(solve_iter(n) if n else 0)
# import sys
# N = int(sys.stdin.readline())
# if not N:
#     sys.stdout.write('0')
#     exit()
# res = ''
# while N:
#     if N%(-2):
#         res = '1' + res
#         N = N//-2 + 1
#     else:
#         res = '0' + res
#         N //= -2
# sys.stdout.write(res)
