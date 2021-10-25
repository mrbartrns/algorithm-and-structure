# BOJ 11657 타임 머신
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def bf(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            cur, nxt, cost = edges[j]
            if (
                distance[cur] < INF and distance[nxt] > distance[cur] + cost
            ):  # 길이 없는데 갈 순 없으므로
                distance[nxt] = distance[cur] + cost
                if i == N - 1:
                    return True
    return False


N, M = map(int, si().split(" "))
edges = []
distance = [INF] * (N + 1)
for _ in range(M):
    a, b, c = map(int, si().split(" "))
    edges.append((a, b, c))

cycle = bf(1)
if cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] < INF:
            print(distance[i])
        else:
            print(-1)
