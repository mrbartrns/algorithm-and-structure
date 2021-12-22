# ALGOSPOT PACKING
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def pack(n, v):
    if cache[n + 1][v] > -1:
        return cache[n + 1][v]
    cache[n + 1][v] = 0
    ret = cache[n + 1][v]
    best_next = -1
    for i in range(n + 1, N):
        if v + volume[i] <= V:
            ret = max(ret, prefer[i] + pack(i, v + volume[i]))
            if ret > cache[n + 1][v]:
                cache[n + 1][v] = ret
                best_next = i
    return cache[n + 1][v]


T = int(si().strip())
for _ in range(T):
    N, V = map(int, si().strip().split(" "))
    prefer = [0] * N
    volume = [0] * N
    tools = [""] * N
    cache = [[-1 for _ in range(V + 1)] for _ in range(N + 1)]
    answer = [[0 for _ in range(V + 1)] for _ in range(N + 1)]
    for i in range(N):
        a, b, c = list(si().strip().split(" "))
        tools[i] = a
        volume[i] = int(b)
        prefer[i] = int(c)
    print(pack(-1, 0))
