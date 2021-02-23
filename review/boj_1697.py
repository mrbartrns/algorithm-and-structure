# BOJ 1697
import sys
from collections import deque

si = sys.stdin.readline

n, m = map(int, si().split())
visited = [0] * 100001


def bfs(start, end):
    que = deque([start])
    while que:
        v = que.popleft()
        if v == end:
            return visited[v]
        if v + 1 <= 100000 and not visited[v + 1]:
            visited[v + 1] = visited[v] + 1
            que.append(v + 1)
        if v - 1 >= 0 and not visited[v - 1]:
            visited[v - 1] = visited[v] + 1
            que.append(v - 1)
        if v * 2 <= 100000 and not visited[v * 2]:
            visited[2 * v] = visited[v] + 1
            que.append(2 * v)


print(bfs(n, m))