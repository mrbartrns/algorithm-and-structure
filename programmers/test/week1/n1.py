"""
1부터 n까지 배열에 모든 숫자가 들어있는지 확인해야 한다.
배열에는 중복된 숫자가 없어야 한다.
"""


def solution(arr: list[int]):
    new_arr = list(set(arr))
    n = len(arr)
    return len(new_arr) == n and sum(new_arr) == (n * (n + 1)) / 2


arr = [4, 1, 3, 2]
arr = [4, 1, 3]
print(solution(arr))
