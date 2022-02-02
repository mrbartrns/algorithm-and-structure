# BOJ 1082 방 번호
import sys

si = sys.stdin.readline

N = int(si().strip())
arr = list(map(int, si().strip().split(" ")))
M = int(si().strip())
cache = [0] * (M + 1)

for i in range(N - 1, -1, -1):
    for j in range(arr[i], M + 1):
        cache[j] = max(cache[j], cache[j - arr[i]] * 10 + i)
print(cache[M])
