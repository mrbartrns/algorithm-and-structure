# kruskal algorithm

def kruskal(n: int, costs: list) -> int:
    """
    kruskal Algorithms
    Args:
        n: number of nodes
        costs: array contains (current_node, next_node, value)

    Returns(int): total amount of minimum value

    """
    costs.sort(key=lambda x: x[2])
    edge = 0
    tot = 0
    parent = [i for i in range(n + 1)]
    for i in range(len(costs)):
        if edge == n - 1:
            # n개의 노드는 최대 n - 1개의 간선을 가질 수 있다
            break
        cur = costs[i][0]
        next_node = costs[i][1]
        cost = costs[i][2]
        if not find_parent(parent, cur, next_node):
            union_parent(parent, cur, next_node)
            tot += cost
            edge += 1
    return tot


def find_parent(parent, cur, next_node):
    cur = get_parent(parent, cur)
    next_node = get_parent(parent, next_node)
    if cur != next_node:
        return False
    return True


def get_parent(parent, node):
    if parent[node] == node:
        return node
    parent[node] = get_parent(parent, parent[node])
    return parent[node]


def union_parent(parent, cur, next_node):
    cur = get_parent(parent, cur)
    next_node = get_parent(parent, next_node)
    if cur < next_node:
        parent[next_node] = cur
    else:
        parent[cur] = next_node
