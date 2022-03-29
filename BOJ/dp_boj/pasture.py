import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

M, N = map(int, si().strip().split(" "))  # 세로, 가로
adj = [list(map(int, si().strip().split(" "))) for _ in range(M)]
cache = [[0 for _ in range(N)] for _ in range(M)]
answer = 0
for i in range(M):
    for j in range(N):
        if adj[i][j]:
            continue
        cache[i][j] = 1
        cache[i][j] += min(
            cache[i - 1][j] if i - 1 >= 0 else 0,
            cache[i][j - 1] if j - 1 >= 0 else 0,
            cache[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0,
        )
        answer = max(answer, cache[i][j])
print(answer)
