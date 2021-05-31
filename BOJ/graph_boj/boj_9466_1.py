# BOJ 9466
n = 7
graph = [0, 3, 1, 3, 7, 3, 4, 6]
visited = [False] * (n + 1)
done = [False] * (n + 1)
cnt = [0]


def dfs(v):
    visited[v] = True
    i = graph[v]
    if not visited[i]:
        dfs(i)
    elif visited[i] and not done[i]:
        j = i
        while j != v:
            j = graph[j]
            cnt[0] += 1
        cnt[0] += 1
    done[v] = True


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

print(n - cnt[0])