import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321

N, M = map(int, si().strip().split(" "))
adj = [list(map(int, si().strip().split(" "))) for _ in range(N)]
cache = [[[INF for _ in range(M)] for _ in range(N)] for _ in range(3)]
for i in range(3):
    for k in range(M):
        cache[i][0][k] = adj[0][k]

for j in range(1, N):
    for k in range(M):
        for i in range(3):
            cache[i][j][k] = min(
                cache[0][j - 1][k - 1] + adj[j][k] if i != 0 and k - 1 >= 0 else INF,
                cache[1][j - 1][k] + adj[j][k] if i != 1 else INF,
                cache[2][j - 1][k + 1] + adj[j][k] if i != 2 and k + 1 < M else INF,
            )

answer = INF
for i in range(3):
    for k in range(M):
        answer = min(answer, cache[i][N - 1][k])
print(answer)
