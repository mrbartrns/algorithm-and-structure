# 이코테 이진탐색 예제문제
"""
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다. 이때 수열에서 x가 등장하는 횟수를 계산하라
"""
n = 7
arr = [1, 1, 2, 2, 2, 2, 3]
x = 2
start = 0
end = n - 1

# 왜 반대로 되는지?
def search_right(start, end, target):
    idx = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            if arr[mid] == target:
                idx = mid
            start = mid + 1  # 작거나 같을 때까지 mid가 증가하기 때문에 가장 높은수를 반환하게 됨
        else:
            end = mid - 1

    return idx


def search_left(start, end, target):
    idx = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            if arr[mid] == target:
                idx = mid
            end = mid - 1
        else:
            start = mid + 1

    return idx


print(search_right(start, end, x))
print(search_left(start, end, x))

# 간단한 방법으로는
from bisect import bisect_left, bisect_right  # 가 있음
