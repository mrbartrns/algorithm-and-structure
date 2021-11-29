"""
트리 구조임을 감안하여 트리 형태로 작성하기
"""

import sys

sys.setrecursionlimit(1000000)
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def dfs(parent, cur):
    leaf = True
    ret = 0
    for child in adj[cur]:
        if child == parent:
            continue
        leaf = False
        ret += dfs(cur, child)

    if leaf:
        if info[cur] == "S":
            return counts[cur]
        return 0

    if info[cur] == "W":
        value = ret - counts[cur]
        return value if value > 0 else 0
    ret += counts[cur]
    return ret


N = int(si())
info = [""] * (N + 1)
counts = [0] * (N + 1)
adj = [[] for _ in range(N + 1)]
distance = [0] * (N + 1)
sheeps = [0] * (N + 1)

for i in range(2, N + 1):
    a, b, c = list(si().strip().split(" "))
    info[i] = a
    counts[i] = int(b)
    adj[i].append(int(c))
    adj[int(c)].append(i)
answer = dfs(-1, 1)
print(answer)
