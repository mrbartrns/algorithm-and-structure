# BOJ 2667
import sys

si = sys.stdin.readline


def dfs(x, y):
    if apts[x][y] == 1:
        apts[x][y] = 0
        cnt[0] += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            dfs(nx, ny)
        return True
    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(si())
apts = []
cnt = [0]
nums = []
ret = 0
for _ in range(n):
    apts.append(list(map(int, si().strip())))
# print(apts)
for i in range(n):
    for j in range(n):
        cnt = [0]
        if dfs(i, j):
            nums.append(cnt[0])
            ret += 1
nums.sort()
print(ret)
print("\n".join(map(str, nums)))