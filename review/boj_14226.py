# BOJ 14226
# https://yabmoons.tistory.com/74
import sys
from collections import deque

si = sys.stdin.readline
MAX = 2001

n = int(si())
visited = [[False for _ in range(MAX)] for _ in range(MAX)]


def bfs(target):
    que = deque()
    que.append((1, 0, 0))  # display, clipboard, cnt
    visited[1][0] = True
    while que:
        display, clipboard, cnt = que.popleft()
        if display == target:
            return cnt

        if display > 0 and display < MAX:
            if not visited[display][display]:
                visited[display][display] = True
                que.append((display, display, cnt + 1))
            if not visited[display - 1][clipboard]:
                visited[display - 1][clipboard] = True
                que.append((display - 1, clipboard, cnt + 1))
            if clipboard > 0 and display + clipboard < MAX:
                if not visited[display + clipboard][clipboard]:
                    visited[display + clipboard][clipboard] = True
                    que.append((display + clipboard, clipboard, cnt + 1))

print(bfs(n))