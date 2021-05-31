# BOJ 15684
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n, m, h = map(int, si().split())
visited = [[False for _ in range(n - 1)] for _ in range(h)]
for _ in range(m):
    a, b = map(int, si().split())
    visited[a - 1][b - 1] = True


def move(graph):
    for x in range(n):
        cur_idx = x
        for y in range(h):
            if cur_idx - 1 >= 0 and graph[y][cur_idx - 1]:
                cur_idx -= 1
            elif cur_idx < n - 1 and graph[y][cur_idx]:
                cur_idx += 1
        if cur_idx != x:
            return False
    return True


def backtrack(start, idx, k):
    if idx == k:
        if move(visited):
            print(k)
            sys.exit(0)
        return
    for i in range(start, h):
        for j in range(n - 1):
            if not visited[i][j]:
                flag = True
                if j - 1 >= 0 and visited[i][j - 1]:
                    flag = False
                if j + 1 < n - 1 and visited[i][j + 1]:
                    flag = False
                if flag:
                    visited[i][j] = True
                    backtrack(i, idx + 1, k)
                    visited[i][j] = False


for i in range(4):
    backtrack(0, 0, i)
print(-1)
