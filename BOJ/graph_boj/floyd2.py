# BOJ 11780 플로이드 2
"""
A도시에서 B도시로 가는데 필요한 비용의 최솟값과 그때의 최소비용에 포함되어 있는 도시의 개수 K 출력
그 다음 도시 i에서 j로 가는 경로를 출력
i에서 j로 갈 수 없는 경우에는 0을 출력
플로이드의 뜻: 어떤 경로 i에서 j로 가는데 있어서 k를 거쳐가는 경로가 가장 빠를 수 있다.
따라서 i -> j 로 가기 위해서는 k를 반드시 거쳐야 한다.
K까지의 경로를 모두 더한후 k에서 j까지 가는 경로를 모두 더한다.
"""
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


N = int(si())
M = int(si())
distance = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
arrival = [[[] for _ in range(N + 1)] for i in range(N + 1)]
for i in range(1, N + 1):
    distance[i][i] = 0
for _ in range(M):
    a, b, c = map(int, si().split(" "))
    distance[a][b] = min(distance[a][b], c)


# floyd
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                arrival[i][j].clear()
                for city in arrival[i][k]:
                    arrival[i][j].append(city)
                arrival[i][j].append(k)
                for city in arrival[k][j]:
                    arrival[i][j].append(city)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(distance[i][j] if distance[i][j] < INF else 0, end=" ")
    print()

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if distance[i][j] == INF or distance[i][j] == 0:
            print(0)
        else:
            print(2 + len(arrival[i][j]), end=" ")
            print(i, end=" ")
            for city in arrival[i][j]:
                print(city, end=" ")
            print(j)
