# BOJ 10653 마라톤2
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


N, K = map(int, si().strip().split(" "))
cache = [[INF for _ in range(K + 1)] for _ in range(N + 1)]
arr = []
for _ in range(N):
    a, b = map(int, si().strip().split(" "))
    arr.append((a, b))
for i in range(K + 1):
    cache[0][i] = 0
for j in range(K + 1):
    for i in range(1, N):
        # 1. 모든 칸을 점프
        cache[i][j] = min(
            cache[i][j],
            abs(arr[i][0] - arr[i - 1][0])
            + abs(arr[i][1] - arr[i - 1][1])
            + cache[i - 1][j],
        )
        # 2. 이전 칸에서 점프하지 않고 이전 특정 칸에서 점프
        for k in range(i - 1):
            if j - (i - k - 1) >= 0:
                cache[i][j] = min(
                    cache[i][j],
                    abs(arr[i][0] - arr[k][0])
                    + abs(arr[i][1] - arr[k][1])
                    + cache[k][j - (i - k - 1)],
                )
print(cache[N - 1][K])
