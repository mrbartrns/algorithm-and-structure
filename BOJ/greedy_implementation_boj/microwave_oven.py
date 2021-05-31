# BOJ 10162
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

n = int(si())
arr = [0, 0, 0]
sec = [300, 60, 10]
for i in range(len(sec)):
    arr[i] = n // sec[i]
    n -= arr[i] * sec[i]

if n > 0:
    print(-1)
else:
    print(" ".join(list(map(str, arr))))
