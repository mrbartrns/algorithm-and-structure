# 그래프 만들기
"""
    5           # 서로 연결된 관계의 수
    1 2
    2 5
    5 1
    3 4
    4 6
"""
# 양방향성 그래프를 만드는데 사용됨
# 단방향성 그래프를 만들 때에는?
def make_graph():
    n = int(input())
    graph = {}

    for _ in range(n):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, []) + [b]  # can only concatenate list to list, not int
        # graph[b] = graph.get(b, []) + [a]

    return graph


def dfs(graph, s):
    to_visit = [s]
    visited = []
    while to_visit:
        u = to_visit.pop()
        visited.append(u)
        for v in graph[u]:
            if v not in visited and v not in to_visit:
                to_visit.append(v)
    return visited


# print(dfs({1: [2, 3], 2: [3, 4, 5], 3: [5, 7, 8], 4:[5], 5: [6], 6: [], 7: [8], 8: []}, 1))
print(make_graph())