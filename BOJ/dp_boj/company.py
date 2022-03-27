import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N, M = map(int, si().strip().split(" "))
arr = list(map(lambda x: x - 1 if x != -1 else -1, map(int, si().strip().split(" "))))
scores = [0] * N
cache = [0] * N

# 같은 직속 상사로부터 여러번 칭찬을 받을 수 있는 경우도 생각해야 한다.
for _ in range(M):
    a, b = map(int, si().strip().split(" "))
    scores[a - 1] += b
for i in range(1, N):
    cache[i] = cache[arr[i]] + scores[i]
print(" ".join(list(map(str, cache))))
