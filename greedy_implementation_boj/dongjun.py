# BOJ 2847
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

n = int(si())
arr = [int(si()) for _ in range(n)]

res = 0
val = arr[-1]
for i in range(n - 2, -1, -1):
    if arr[i] >= val:
        if val == 1:
            continue
        val -= 1
        res += arr[i] - val
        arr[i] = val
    else:
        val = arr[i]

print(res)
