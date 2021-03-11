def solution(n, results):
    def dfs(node):
        visited[node] = True
        hs.add(node)
        for i in range(len(graph[node])):
            v = graph[node][i]
            if not visited[v]:
                dfs(v)

    graph = [[] for _ in range(n + 1)]
    ret = []
    flag = True

    for x, y in results:
        graph[x].append(y)

    for i in range(1, n + 1):
        visited = [False for _ in range(n + 1)]
        hs = set()
        if graph[i]:
            dfs(i)
            ret.append(hs)

        for i in range(1, len(visited)):
            if not visited[i]:
                flag = False
                break

        if flag:
            break

    if not flag:
        res = set([i for i in range(1, n + 1)])
        for i in range(len(ret)):
            res = res & ret[i]

        ans = len(res)
        return ans
    else:
        return n


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))