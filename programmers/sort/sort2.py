arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def merge_sort(arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    ret = arr[:]
    left = start
    right = mid + 1
    idx = start
    while left <= mid and right <= end:
        if arr[left] < arr[right]:
            ret[idx] = arr[left]
            left += 1
            idx += 1
        else:
            ret[idx] = arr[right]
            right += 1
            idx += 1

    while left <= mid:
        ret[idx] = arr[left]
        left += 1
        idx += 1

    while right <= end:
        ret[idx] = arr[right]
        right += 1
        idx += 1

    for i in range(start, end + 1):
        arr[i] = ret[i]


def quick_sort(arr, start, end):
    if start >= end:
        return
    left = start + 1
    right = end
    pivot = start
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


# merge_sort(arr, 0, len(arr) - 1)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
