# BOJ 9466
import sys

sys.setrecursionlimit(100001)
si = sys.stdin.readline


def dfs(v):
    visited[v] = True
    if not visited[team[v]]:
        dfs(team[v])
    elif visited[team[v]] and not done[team[v]]:
        j = team[v]
        while j != v:
            cnt[0] += 1
            j = team[j]
        cnt[0] += 1
    # v가 바뀌면 안됨
    done[v] = True


t = int(si())
for _ in range(t):
    n = int(si())
    team = [0] + list(map(int, si().split()))
    visited = [False] * (n + 1)
    done = [False] * (n + 1)
    cnt = [0]
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    print(n - cnt[0])