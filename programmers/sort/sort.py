# 정렬 총정리 -> 설명까지 조금 덧붙여보자
# bubble sort
from re import M


def bubble_sort(arr):
    for _ in range(len(arr)):
        flag = True
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break


# selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# inserction sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


# merge sort
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
            idx += 1
            left += 1
        else:
            ret[idx] = arr[right]
            idx += 1
            right += 1

    while left <= mid:
        ret[idx] = arr[left]
        idx += 1
        left += 1

    while right <= end:
        ret[idx] = arr[right]
        idx += 1
        right += 1

    for i in range(start, end + 1):
        arr[i] = ret[i]


# quick sort
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
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# merge_sort(arr, 0, len(arr) - 1)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
