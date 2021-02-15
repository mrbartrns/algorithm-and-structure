# BOJ 5014
import sys
from collections import deque

"""
총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층
강호가 지금 있는 곳은 S층이고 G층으로 이동하려고함
U버튼은 U층을 가는 버튼, D 버튼은 아래로 D층을 가는 버튼
G층에 도착하기 위해서는 버튼을 적어도 몇번 눌러야하는지 구하는 프로그램 작성
"""

si = sys.stdin.readline


def bfs(s, g):
    que = deque([(s, 0)])

    while que:
        v, cnt = que.popleft()
        if not visited[v]:
            visited[v] = True

            if v == g:
                return cnt

            if v + u <= f:
                que.append((v + u, cnt + 1))

            if v - d >= 1:
                que.append((v - d, cnt + 1))

    return -1


f, s, g, u, d = map(int, si().split())
visited = [False] * (f + 1)
value = bfs(s, g)
print(value if value > -1 else "use the stairs")