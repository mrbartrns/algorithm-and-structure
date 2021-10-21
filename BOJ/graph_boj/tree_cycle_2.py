# BOJ 4803 트리
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def get_parent(arr, a):
    if arr[a] == a:
        return a
    arr[a] = get_parent(arr, arr[a])
    return arr[a]


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


tc = 0
while True:
    N, M = map(int, si().split(" "))
    if N == 0 and M == 0:
        break
    tc += 1
    parents = [i for i in range(N + 1)]
    is_tree = [True] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, si().split(" "))
        if (
            get_parent(parents, a) != get_parent(parents, b)
            and is_tree[a]
            and is_tree[b]
        ):
            union_parent(parents, a, b)
        else:
            p = get_parent(parents, a)
            q = get_parent(parents, b)
            is_tree[p] = False
            is_tree[q] = False

    cnt = 0
    for i in range(1, N + 1):
        if is_tree[get_parent(parents, i)]:
            cnt += 1
            is_tree[get_parent(parents, i)] = False
    answer = ""
    if cnt == 0:
        answer = "No trees."
    elif cnt == 1:
        answer = "There is one tree."
    else:
        answer = "A forest of " + str(cnt) + " trees."
    print(f"Case {tc}: {answer}")
