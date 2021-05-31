# BOJ 1168
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]


def solve(n, k, arr):
    ret = []
    i = 0
    while arr:
        i = (i + (k - 1)) % len(arr)
        el = arr.pop(i)
        ret.append(el)
    return ret


ret = solve(n, k, arr)
string = "<"
string += ", ".join(map(str, ret))
string += ">"


print(string)
