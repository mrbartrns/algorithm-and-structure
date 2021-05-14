"""
Union Find Algorithms
"""


# get_parent
def get_parent(arr, idx):
    if arr[idx] == idx:
        return idx
    arr[idx] = get_parent(arr, arr[idx])
    return arr[idx]


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


def find_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    return True if a == b else False


def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    tot = 0
    for i in range(len(costs)):
        u, v, cost = costs[i]
        if not find_parent(parent, u, v):
            union_parent(parent, u, v)
            tot += cost
    return tot


if __name__ == "__main__":
    n = 4
    costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    print(solution(n, costs))
