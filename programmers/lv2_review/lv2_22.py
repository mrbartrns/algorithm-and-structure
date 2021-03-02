# 타겟 넘버
from bisect import bisect_left, bisect_right


def solution(numbers, target):
    res = []
    dfs(numbers, res, 0, 0)
    res.sort()
    return bisect_right(res, target) - bisect_left(res, target)


def dfs(org, arr, idx, s):
    if idx == len(org):
        arr.append(s)
        return

    dfs(org, arr, idx + 1, s - org[idx])
    dfs(org, arr, idx + 1, s + org[idx])


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))