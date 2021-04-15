# combination and permutation

"""
def combinations(arr, r):
    for y in range(len(arr)):
        if r == 1:
            yield [arr[y]]
        else:
            for next in combinations(arr[y + 1 :], r - 1):
                yield [arr[y]] + next


for combi in combinations([1, 2, 3, 4, 5], 2):
    print(combi)
"""


def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i + 1 :], r - 1):
                yield [arr[i]] + next


def permutation(prefix, k):
    if r == k:
        yield prefix
    else:
        for i in range(k, len(arr)):
            arr[i], arr[k] = arr[k], arr[i]
            for next in permutation(prefix + [arr[i]], k + 1):
                yield next
            arr[i], arr[k] = arr[k], arr[i]


arr = [0] * 500000
r = 2
print(list(combination(arr, r)))
