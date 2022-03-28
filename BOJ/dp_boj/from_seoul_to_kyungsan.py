import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N, K = map(int, si().strip().split(" "))
cache = [[0 for _ in range(K + 1)] for _ in range(N)]
arr = [[0 for _ in range(2)] for _ in range(N)]
for i in range(N):
    a, b, c, d = map(int, si().strip().split(" "))
    arr[i][0] = (a, b)
    arr[i][1] = (c, d)

for i in range(2):
    t, v = arr[0][i]
    cache[0][t] = max(v, cache[0][t])
for i in range(1, N):
    walk_time, walk_value = arr[i][0]
    bicycle_time, bicycle_value = arr[i][1]
    for j in range(K + 1):
        if j - walk_time >= 0 and cache[i - 1][j - walk_time] > 0:
            cache[i][j] = max(cache[i][j], cache[i - 1][j - walk_time] + walk_value)
        if j - bicycle_time >= 0 and cache[i - 1][j - bicycle_time] > 0:
            cache[i][j] = max(
                cache[i][j], cache[i - 1][j - bicycle_time] + bicycle_value
            )

print(max(cache[N - 1]))
