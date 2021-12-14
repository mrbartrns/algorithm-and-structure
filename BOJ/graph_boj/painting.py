# BOJ 1029
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline


def own(mask, cost, artist):
    if mask & (1 << artist):
        return 0
    if cache[mask][cost][artist] > -1:
        return cache[mask][cost][artist]
    cache[mask][cost][artist] = 0
    for nxt in range(N):
        if adj[artist][nxt] >= cost:
            cache[mask][cost][artist] = max(
                cache[mask][cost][artist],
                own(mask | (1 << artist), adj[artist][nxt], nxt),
            )
    cache[mask][cost][artist] += 1
    return cache[mask][cost][artist]


N = int(si().strip())
adj = [list(map(int, list(si().strip()))) for _ in range(N)]
cache = [[[-1 for _ in range(N)] for _ in range(10)] for _ in range(1 << N)]

print(own(0, 0, 0))
