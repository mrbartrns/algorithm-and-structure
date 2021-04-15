def bfs(graph, root, end):
    visited = []
    to_visit = [root]
    n = 0
    while to_visit:
        n += 1
        u = to_visit.pop(0)
        visited.append(u)
        if end in visited:
            print(n)
            return visited
        for i in graph[u]:
            if i not in visited and i not in to_visit:
                to_visit.append(i)
    return visited


def dfs(graph, stack, end, answer):
    if end in stack:
        answer[0] = len(stack) - 1
        return
    else:
        u = stack[-1]
        for i in graph[u]:
            if i not in stack:
                stack.append(i)
                dfs(graph, stack, end, answer)
                stack.pop()


# t = int(input())
# for y in range(t):
#     graph = {}
#     node, seg = map(int, input().split())
#     for _ in range(seg):
#         a, b = map(int, input().split())
#         graph[a] = graph.get(a, []) + [b]
#         # if b not in graph:
#         #     graph[b] = []
#         graph[b] = graph.get(b, []) + [a]
#     for x in range(1, node + 1):
#         if x not in graph:
#             graph[x] = []
#     # print(graph)
#     start, end = map(int, input().split())
#     to_visit = [start]
#     answer = [0]
#     dfs(graph, to_visit, end, answer)
#     print(f"#{y + 1} {answer[0]}")
#     # print(f"#{y + 1} {bfs(graph, start, end)}")

graph_a = {1: [3, 4], 2: [3, 5], 3: [1, 2], 4: [1, 6], 5: [2], 6: [4]}
# graph_b = {1: [6], 2: [3, 6], 3: [5], 4: [], 5: [3], 6: [1, 2], 7: []}
print(bfs(graph_a, 1, 6))
# visited = []
# to_visit = [4]
# answer = [0]
# dfs(graph_a, to_visit, 5, answer)
# print(answer)
