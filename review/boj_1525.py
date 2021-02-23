# BOJ 1525
import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(v):
    que = deque([(v, 0)])
    visited.add(v)
    while que:
        v, cnt = que.popleft()
        if v == ANS:
            return cnt

        z = v.find("0")
        x = z // 3
        y = z % 3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue
            temp = list(v)
            temp[x * 3 + y], temp[nx * 3 + ny] = temp[nx * 3 + ny], temp[x * 3 + y]
            str_temp = "".join(temp)
            if str_temp not in visited:
                visited.add(str_temp)
                que.append((str_temp, cnt + 1))
    return -1


ANS = "123456780"
visited = set()
graph = []
for _ in range(3):
    graph.extend(list(si().split()))
v = "".join(graph)
sys.stdout.write(str(bfs(v)))
