# BOJ 1068 트리
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def dfs(node, banned):
    leaf = True
    count = 0
    if node == banned:
        return count
    for nxt in graph[node]:
        count += dfs(nxt, banned)
        if nxt == banned:
            continue
        leaf = False
    if leaf:
        return 1
    return count


N = int(si())
arr = list(map(int, si().split(" ")))
banned = int(si())
graph = [[] for _ in range(N)]
root = 0
for i in range(N):
    if arr[i] == -1:
        root = i
        continue
    graph[arr[i]].append(i)
print(dfs(root, banned))
