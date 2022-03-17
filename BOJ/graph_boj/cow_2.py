# BOJ 10653 마라톤2
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def solve():
    q = []
    heapq.heappush(q, (0, 0, 0))
    cache[0][0] = 0
    while q:
        dist, n, k = heapq.heappop(q)
        if cache[n][k] > dist:
            continue
        if n >= N or k >= K + 1:
            continue
        if n + 1 < N:
            cost = (
                abs(arr[n][0] - arr[n + 1][0]) + abs(arr[n][1] - arr[n + 1][1]) + dist
            )
            if cache[n + 1][k] > cost:
                cache[n + 1][k] = cost
                heapq.heappush(q, (cost, n + 1, k))
        for i in range(n + 2, N):
            cost = abs(arr[n][0] - arr[i][0]) + abs(arr[n][1] - arr[i][1]) + dist
            if k + i - n - 1 < K + 1 and cache[i][k + i - n - 1] > cost:
                cache[i][k + i - n - 1] = cost
                heapq.heappush(q, (cost, i, k + i - n - 1))


N, K = map(int, si().strip().split(" "))
arr = []
for _ in range(N):
    a, b = map(int, si().strip().split(" "))
    arr.append((a, b))
cache = [[INF for _ in range(K + 1)] for _ in range(N + 1)]
solve()
print(cache[N - 1][K])
