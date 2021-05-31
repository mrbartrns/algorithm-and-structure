# BOJ 9466
import sys

sys.setrecursionlimit(1000000)
si = sys.stdin.readline


def dfs(graph, v):
    visited[v] = True
    i = graph[v]
    if not visited[i]:
        dfs(graph, i)
    else:
        if not done[i]:
            j = i
            while j != v:
                cnt[0] += 1
                j = graph[j]
            cnt[0] += 1
    done[v] = True


t = int(si())
for _ in range(t):
    n = int(si())
    arr = list(map(int, si().split()))

    # start로 돌아오지 않으면 False, start로 돌아올 수 있다면 True > False의 갯수를 센다.
    cnt = [0]
    arr = [0] + arr
    visited = [False] * (n + 1)
    done = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(arr, i)

    print(n - cnt[0])