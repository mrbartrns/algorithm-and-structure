"""
Union find algorithm
"""


def get_parent(arr, i):
    if arr[i] == i:
        return i
    arr[i] = get_parent(arr, arr[i])
    return arr[i]


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
    return 1 if a == b else 0


parent = [i for i in range(11)]
union_parent(parent, 1, 2)
print(parent)
union_parent(parent, 2, 3)
print(parent)
union_parent(parent, 3, 4)
print(parent)
union_parent(parent, 5, 6)
print(parent)
union_parent(parent, 6, 7)
print(parent)
union_parent(parent, 7, 8)
print(parent)

print(find_parent(parent, 1, 5))
union_parent(parent, 1, 5)
print(find_parent(parent, 1, 5))
