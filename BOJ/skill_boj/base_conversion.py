# BOJ 11576
import sys

input = sys.stdin.readline


def solve_rec(arr, a):
    num = 0
    for i in range(len(arr)):
        num += arr[i] * (a ** (len(arr) - i - 1))
    return num


def solve(n, b):
    if n // b == 0:
        return [str(n % b)]
    t = solve(n // b, b) + [str(n % b)]
    return t


a, b = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))
num = solve_rec(arr, a)
print(" ".join(solve(num, b)))
