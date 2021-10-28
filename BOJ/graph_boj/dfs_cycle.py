# dfs 사이클 탐색 알고리즘


def dfs(node):
    discovered[node] = counter[0]
    counter[0] += 1
    for nxt in graph[node]:
        print(f"{node, nxt} is a ")
        if discovered[nxt] == -1:
            print("tree edge")
            dfs(nxt)
        # nxt가 더 크다면, 순방향 간선 (단 트리 간선은 아님)
        elif discovered[node] < discovered[nxt]:
            print("foward edge")
        # next가 더 작다면, 역방향 간선
        elif not finished[nxt]:
            print("back edge")
        else:
            print("cross edge")
    finished[node] = True


graph = [[1, 2, 6, 9], [3, 6], [7], [2, 4, 5], [5], [7], [], [0], [], [4]]
discovered = [-1] * 10
finished = [False] * 10
counter = [1]
dfs(0)
print(discovered)
