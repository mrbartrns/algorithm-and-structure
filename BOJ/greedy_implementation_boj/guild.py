# greedy 대표유형


n = int(input())
arr = list(map(int, input().split()))

# n = 5
# arr = [2, 3, 1, 2, 2]
arr.sort()


def solve(arr):
    res = 0
    mod = 1
    for i in range(len(arr)):
        if arr[i] // mod > 1 or (arr[i] // mod == 1 and arr[i] % mod > 0):
            mod += 1
        else:
            mod = 1
            res += 1
    return res


def sol_ref(arr):
    res = 0
    mod = 0
    for i in range(len(arr)):
        mod += 1
        if mod >= arr[i]:
            res += 1
            mod = 0
    return res


print(solve(arr))
print(sol_ref(arr))