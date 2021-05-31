# BOJ 16928
import sys
from collections import deque

si = sys.stdin.readline

visited = [False] * 101
game_board = [0] * 101


def bfs(arr):
    que = deque()
    que.append((1, 0))
    visited[1] = True
    while que:
        idx, cnt = que.popleft()
        if idx == 100:
            return cnt
        for i in range(7):
            n_idx = idx + i
            if n_idx > 100:
                continue
            if arr[n_idx] == 0 and not visited[n_idx]:
                visited[n_idx] = True
                que.append((n_idx, cnt + 1))
            elif arr[n_idx] > 0 and not visited[n_idx] and not visited[arr[n_idx]]:
                visited[arr[n_idx]] = True
                que.append((arr[n_idx], cnt + 1))


n, m = map(int, si().split())
for _ in range(n):
    a, b = map(int, si().split())
    game_board[a] = b
for _ in range(m):
    a, b = map(int, si().split())
    game_board[a] = b

res = bfs(game_board)
print(res)
