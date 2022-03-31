# BOJ 17404 RGB 거리 2
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321
N = int(si().strip())
arr = [list(map(int, si().strip().split(" "))) for _ in range(N)]
# cache[current_index][color_choice][first_color_choice]
cache = [[[INF for _ in range(3)] for _ in range(3)] for _ in range(N)]


cache[0][0][0] = arr[0][0]
cache[0][1][1] = arr[0][1]
cache[0][2][2] = arr[0][2]

for i in range(1, N):
    for k in range(3):
        cache[i][0][k] = min(cache[i - 1][1][k], cache[i - 1][2][k]) + arr[i][0]
        cache[i][1][k] = min(cache[i - 1][0][k], cache[i - 1][2][k]) + arr[i][1]
        cache[i][2][k] = min(cache[i - 1][0][k], cache[i - 1][1][k]) + arr[i][2]
answer = INF
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        answer = min(answer, cache[N - 1][i][j])
print(answer)
