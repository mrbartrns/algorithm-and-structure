import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def get_parent(arr, a):
    if a == arr[a]:
        return a
    arr[a] = get_parent(arr, arr[a])
    return a


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


n = int(si())
m = int(si())
arr = [int(si()) for _ in range(m)]
parents = [i for i in range(n + 1)]
cnt = 0
for i in range(len(arr)):
    data = get_parent(parents, arr[i])
    if data != 0:
        union_parent(parents, data, data - 1)
        cnt += 1
    else:
        break
print(cnt)