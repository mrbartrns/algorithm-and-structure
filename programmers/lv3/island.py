# 섬 연결하기

def solution(n, costs):
    # sort 안하면 틀림
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    edge = 0
    tot = 0
    for i in range(len(costs)):
        if edge == n - 1:
            break
        u, v, cost = costs[i]
        if not find_parent(parent, u, v):
            union_parent(parent, u, v)
            tot += cost
            edge += 1
    return tot


def find_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    return True if a == b else False


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


def get_parent(arr, i):
    if arr[i] == i:
        return arr[i]
    arr[i] = get_parent(arr, arr[i])
    return arr[i]


if __name__ == "__main__":
    n = 4
    costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    print(solution(n, costs))
