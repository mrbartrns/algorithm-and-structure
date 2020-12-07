from circle_queue import CQueue

# size = 5
# queue = CQueue(5)

graph_list = {1: [3, 4], 2: [3, 4, 5], 3: [1, 5], 4: [1], 5: [2, 6], 6: [3, 5]}


def bfs(tree: dict or list, root):
    size = len(tree)  # size is number of nodes
    to_visit = CQueue(size)
    visited = []
    to_visit.enqueue(root)
    while not to_visit.isEmpty():
        t = to_visit.dequeue()
        if t not in visited:
            visited.append(t)
        for i in tree[t]:
            if i not in visited:
                to_visit.enqueue(i)
    return visited


# 그냥 복습차 > dfs는 재귀로도 구현이 가능
def dfs(tree: dict or list, root):
    to_visit = [root]  # stack
    visited = []
    while to_visit:
        v = to_visit.pop()
        if v not in visited:
            visited.append(v)
        for i in tree[v]:
            if i not in visited:
                to_visit.append(i)
    return visited


root = 1
stack = [root]
visited = []

# 재귀로 구현한 dfs
def dfs_rec(tree, root, stack, visited):
    if not stack:
        return
    else:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for i in tree[v]:
                stack.append(i)
        dfs_rec(tree, root, stack, visited)


print(bfs(graph_list, 1))
print(dfs(graph_list, 1))
dfs_rec(graph_list, root, stack, visited)
print(visited)