# BOJ 5624 좋은 수
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

cache = [False] * (400001)

N = int(si().strip())
arr = list(map(int, si().strip().split(" ")))
answer = 0
for i in range(N):
    for j in range(i):
        if cache[arr[i] - arr[j] + 200000]:
            answer += 1
            break
    for j in range(i + 1):
        cache[arr[i] + arr[j] + 200000] = True
print(answer)
