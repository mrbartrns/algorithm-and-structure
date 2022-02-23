# BOJ 2643
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def solve(idx, length):
    if idx >= N:
        return 0
    if cache[idx][length] > -1:
        return cache[idx][length]
    cache[idx][length] = 0
    if length >= arr[idx][1]:
        cache[idx][length] = max(cache[idx][length], 1 + solve(idx + 1, arr[idx][1]))
    cache[idx][length] = max(cache[idx][length], solve(idx + 1, length))
    return cache[idx][length]


N = int(si().strip())
arr = []
cache = [[-1 for _ in range(1001)] for _ in range(101)]
for _ in range(N):
    a, b = map(int, si().strip().split(" "))
    if a < b:
        a, b = b, a
    arr.append((a, b))
arr.sort(key=lambda x: (-x[0], -x[1]))
solve(0, 1000)
print(cache[0][1000])
