# 퀵소트

def quicksort(arr, start, end):
    if start >= end:
        return

    left = start + 1
    pivot = start
    right = end
    while left <= right:
        while left < len(arr) and arr[left] <= arr[pivot]:
            left += 1
        while right >= 0 and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quicksort(arr, start, right - 1)
    quicksort(arr, right + 1, end)
