# 섬 연결하기
"""
크루스칼 알고리즘
크루스칼 알고리즘은 그리디 알고리즘 형식의 최단 경로 탐색 알고리즘
기본적으로 union-find 패러다임을 사용
"""


def solution(n, costs):
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    idx = 0
    tot = 0
    for i in range(len(costs)):
        a, b, c = costs[i]
        if not find_parent(parent, a, b):
            union_parent(parent, a, b)
            tot += c
            idx += 1
        if idx == n - 1:
            break
    return tot


def get_parent(arr, a):
    if a == arr[a]:
        return a
    # 통일되어 있지 않은 부모를 일치시키기 위함
    arr[a] = get_parent(arr, arr[a])
    return arr[a]


def find_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    return a == b


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
