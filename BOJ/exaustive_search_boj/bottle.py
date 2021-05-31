# BOJ 2251
import sys
from collections import deque

si = sys.stdin.readline

a, b, c = map(int, si().split())
# 물의 양을 체크하기 위한 배열(a, b)
check = [[0 for _ in range(201)] for _ in range(201)]


def do(s1, s2, que):
    if check[s1][s2] == 0:
        check[s1][s2] = 1
        que.append((s1, s2))


def bfs(a, b, c):
    r = []
    que = deque()
    que.append((0, 0))
    while que:
        a1, b1 = que.popleft()
        c1 = c - a1 - b1
        if check[a1][b1] == 1:
            continue

        check[a1][b1] = 1
        if a1 == 0:
            r.append(c1)

        if a1 + b1 > b:  # a에서 b로 보낼때 합친 물의 양이 작으면 완전히 비워진다
            que.append((a1 - (b - b1), b))
        else:  # 완전히 비지 않을 경우 a에 남아있는 물의 양은
            que.append((0, a1 + b1))

        if a1 + c1 > c:
            que.append((a1 - (c - c1), b1))
        else:
            que.append((0, b1))

        if b1 + a1 > a:  # b -> a
            que.append((a, b1 - (a - a1)))
        else:
            que.append((a1 + b1, 0))

        if b1 + c1 > c:  # b -> c
            que.append((a1, b1 - (c - c1)))
        else:
            que.append((a1, 0))

        if c1 + a1 > a:  # c -> a
            que.append((a, b1))
        else:
            que.append((a1 + c1, b1))
        if c1 + b1 > b:
            que.append((a1, b))
        else:
            que.append((a1, b1 + c1))
    r.sort()
    return r


sys.stdout.write(" ".join(list(map(str, bfs(a, b, c)))))
