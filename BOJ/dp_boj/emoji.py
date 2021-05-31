# BOJ 14226
import sys
from collections import deque

si = sys.stdin.readline


def bfs(target):
    que = deque()
    que.append((1, 0, 0))
    visited[1][0] = True
    while que:
        display, clip, cnt = que.popleft()
        if display == target:
            return cnt
        if 0 < display < MAX:
            if not visited[display][display]:
                visited[display][display] = True
                que.append((display, display, cnt + 1))
            if not visited[display - 1][clip]:
                visited[display - 1][clip] = True
                que.append((display - 1, clip, cnt + 1))
        if clip > 0 and display + clip < MAX:
            if not visited[display + clip][clip]:
                visited[display + clip][clip] = True
                que.append((display + clip, clip, cnt + 1))


MAX = 2000
visited = [[False for _ in range(MAX)] for _ in range(MAX)]
n = int(si())
print(bfs(n))
