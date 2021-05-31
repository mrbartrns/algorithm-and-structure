# BOJ 9613
import sys

input = sys.stdin.readline


def get_gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return get_gcd(b, a % b)


def solve(idx):
    if len(temp) == 2:
        gcd = get_gcd(temp[0], temp[1])
        sum_arr.append(gcd)
        return
    for i in range(idx + 1, len(arr)):
        idx = i
        temp.append(arr[i])
        solve(idx)
        temp.pop()


t = int(input())
for _ in range(t):
    a, *arr = map(int, input().split())
    sum_arr = []
    temp = []
    solve(-1)
    print(sum(sum_arr))