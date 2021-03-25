# BOJ 15684
import sys

si = sys.stdin.readline


def backtrack(arr, k, n):
    if k == n:
        ladders.append(arr[:])
        return
    for i in range(1, len(graph) - 1):
        for j in range(2, len(graph[0])):
            flag = True
            if j % 2 == 1 and graph[i][j] == -1:
                if i - 1 >= 1 and graph[i - 1][j] >= 0:
                    flag = False
                if i + 1 < len(graph) - 1 and graph[i + 1][j] >= 0:
                    flag = False
                if j - 2 >= 2 and graph[i][j - 2] >= 0:
                    flag = False
                if j + 2 < len(graph[0]) and graph[i][j + 2] >= 0:
                    flag = False
                if flag:
                    arr.append((i, j))
                    graph[i][j] = 0
                    backtrack(arr, k + 1, n)
                    graph[i][j] = -1
                    arr.pop()


def dfs(x, y, i):
    graph[x][y] = i
    if y - 1 >= 0 and graph[x][y - 1] >= 0:
        dfs(x, y - 1, i)
    elif y + 1 < len(graph[0]) and graph[x][y + 1] >= 0:
        dfs(x, y + 1, i)
    elif x + 1 < len(graph) and graph[x + 1][y] >= 0:
        dfs(x + 1, y, i)


n, m, h = map(int, si().split())
arr = []
ladders = []
flag = True

# 그래프 만들기
graph = [[-1 for _ in range(2 * n + 1)] for _ in range(h + 2)]
for j in range(1, n + 1):
    for i in range(h + 2):
        graph[i][2 * j] = 0

# 경로만들기
for _ in range(m):
    h, w = map(int, si().split())
    graph[h][2 * w + 1] = 0

# 백트래킹하기
if m > 0:
    for i in range(3):
        backtrack(arr, 0, i + 1)


# dfs로 경로 탐색하기
for i in range(2, len(graph[0])):
    if i % 2 == 0:
        dfs(0, i, i)

for i in range(2, len(graph[0])):
    if graph[h + 1][i] != graph[0][i]:
        print("no")
        flag = False
        break
if flag:
    print("yes")
