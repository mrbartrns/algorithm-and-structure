def solution(n, costs):
    edges = 0
    tot = 0
    parents = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    for i in range(len(costs)):
        a, b, c = costs[i]
        if not find_parent(parents, a, b):
            union_parent(parents, a, b)
            edges += 1
            tot += c

        if edges == n - 1:
            break
    return tot


def get_parent(arr, a):
    if arr[a] == a:
        return a
    arr[a] = get_parent(arr, arr[a])
    return arr[a]


def find_parent(arr, a, b):
    return get_parent(arr, a) == get_parent(arr, b)


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


if __name__ == "__main__":
    n = 4
    costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    print(solution(n, costs))
