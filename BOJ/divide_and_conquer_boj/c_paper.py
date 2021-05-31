# BOJ 2630
import sys

si = sys.stdin.readline


def solve(x, y, k):
    if k == 1:
        cnt[graph[x][y]] += 1
        return

    flag = True
    el = graph[x][y]
    for i in range(x, x + k):
        for j in range(y, y + k):
            if el != graph[i][j]:
                flag = False
                break

    if flag:
        cnt[el] += 1
        return
    for i in range(2):
        for j in range(2):
            solve(x + i * (k // 2), y + j * (k // 2), k // 2)


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
cnt = [0, 0]
solve(0, 0, n)
print("\n".join(list(map(str, cnt))))