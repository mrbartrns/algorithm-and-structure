# BOJ 7568
import sys

si = sys.stdin.readline
n = int(si())
infos = []

for _ in range(n):
    w, h = map(int, si().split())
    infos.append((w, h))

for i in range(n):
    k = 1
    for j in range(n):
        if infos[i][0] < infos[j][0] and infos[i][1] < infos[j][1]:
            k += 1
    print(k, end=" ")
