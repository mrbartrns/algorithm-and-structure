"""
연결 리스트를 활용한 정렬: 병합정렬
여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
자료를 최소단위의 문제까지 나눈 후에 차례대로 정렬하여 최종결과를 얻어냄
Top-Down 정렬방식
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)


def merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        # if - else로 처리해야하고 if if는 index range에 의해 불가능
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i < len(left):
        res.extend(left[i:])
    if j < len(right):
        res.extend(right[j:])

    return res


print(merge_sort([2, 1, 3, 5, 4]))