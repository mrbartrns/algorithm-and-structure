# BOJ 12869 뮤탈리스크
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


N = int(si().strip())
q = list(map(int, si().strip().split(" ")))
p = [[1, 3, 9], [1, 9, 3], [3, 1, 9], [3, 9, 1], [9, 1, 3], [9, 3, 1]]
while len(q) < 3:
    q.append(0)
cache = [
    [[INF for _ in range(q[2] + 1)] for _ in range(q[1] + 1)] for _ in range(q[0] + 1)
]
cache[0][0][0] = 0

for i in range(len(cache)):
    for j in range(len(cache[0])):
        for k in range(len(cache[0][0])):
            if i == 0 and j == 0 and k == 0:
                continue
            for s in p:
                cache[i][j][k] = min(
                    cache[i][j][k],
                    1
                    + cache[i - s[0] if i - s[0] >= 0 else 0][
                        j - s[1] if j - s[1] >= 0 else 0
                    ][k - s[2] if k - s[2] >= 0 else 0],
                )
print(cache[q[0]][q[1]][q[2]])
