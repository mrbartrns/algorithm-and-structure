# BOJ 14867 물통
"""
물통에 원하는 만큼의 물을 채운다.
처음 상태: 비어있는 상태에서 시작
명령어: 물통 A에 물을 가득 채우기, 물통 X의 물을 버리기, 물통 X의 물을 Y에 붓기
if 물통 X에 남아있는 물의 양이 물통 Y에 남아있는 빈 공간보다 적거나 같다면, 물통 X의 물을 모두 Y에 붓는다.
elif X > Y: 물통 Y에 물을 꽉 채우고 남은 물을 X에 남기기
물통 A의 용량, 물통 B의 용량, 최종상태에서 물통 A에 남겨야 하는 용량, 최종 상태에서 물통 B에 남겨야 하는 용량
"""
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def bfs():
    q = deque()
    visited = set()
    visited.add((0, 0))
    q.append((0, 0, 0))  # y, x, cnt
    while q:
        y, x, cnt = q.popleft()
        if y == EA and x == EB:
            return cnt
        # y -> fill, y -> empty
        if (A, x) not in visited:
            visited.add((A, x))
            q.append((A, x, cnt + 1))
        if (0, x) not in visited:
            visited.add((0, x))
            q.append((0, x, cnt + 1))
        # x -> fill, x -> empty:
        if (y, B) not in visited:
            visited.add((y, B))
            q.append((y, B, cnt + 1))
        if (y, 0) not in visited:
            visited.add((y, 0))
            q.append((y, 0, cnt + 1))
        # move water from y to x
        # 물통 A에 남아있는 물의 양과 물통 B에 남아있는 물의 양 비교
        x_left = B - x
        if y <= x_left:
            ny, nx = 0, x + y
            if (ny, nx) not in visited:
                visited.add((ny, nx))
                q.append((ny, nx, cnt + 1))
        else:
            ny, nx = y - x_left, B
            if (ny, nx) not in visited:
                visited.add((ny, nx))
                q.append((ny, nx, cnt + 1))
        # move water from x to y
        y_left = A - y
        if x <= y_left:
            ny, nx = y + x, 0
            if (ny, nx) not in visited:
                visited.add((ny, nx))
                q.append((ny, nx, cnt + 1))
        else:
            ny, nx = A, x - y_left
            if (ny, nx) not in visited:
                visited.add((ny, nx))
                q.append((ny, nx, cnt + 1))
    return -1


A, B, EA, EB = map(int, si().split(" "))
print(bfs())
