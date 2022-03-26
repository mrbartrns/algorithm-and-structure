# BOJ 14002 가장 긴 증가하는 부분 수열 4
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si().strip())
arr = list(map(int, si().strip().split(" ")))
cache = [1] * N
ret = []


for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            cache[i] = max(cache[i], cache[j] + 1)

# 여기서 자꾸 에러가 났음
max_count = max(cache)
print(max_count)
for i in range(N - 1, -1, -1):
    if cache[i] == max_count:
        ret.append(arr[i])
        max_count -= 1

for i in range(len(ret) - 1, -1, -1):
    print(ret[i], end=" ")
