# 퀵소트 복습하기

def quick_sort(arr, start, end):
    if start >= end:
        return
    left = start + 1
    right = end
    pivot = start
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        while right >= start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)
