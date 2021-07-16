# BOJ 18310 (안테나)
import sys

sys.stdin = open('../input.txt')
si = sys.stdin.readline

INF = 987654321
n = int(si())
arr = list(map(int, si().split()))

arr.sort()
mid = len(arr) // 2
if len(arr) % 2 == 0:
    print(arr[mid - 1])
else:
    print(arr[mid])
