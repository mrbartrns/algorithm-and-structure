# quick_sort -> 한번 더 복습 필요
def quick_sort(arr, begin, end):
    p = partition(arr, begin, end)
    quick_sort(arr, begin, p - 1)
    quick_sort(arr, p + 1, end)


def partition(arr, begin, end):
    pivot = (begin + end) // 2
    left = begin
    right = end
    while left < right:
        while left < right and arr[left] < arr[pivot]:
            left += 1
        while left < right and arr[right] >= arr[pivot]:
            right -= 1
        if left < right:
            if left == pivot:
                pivot = right
            arr[left], arr[right] = arr[right], arr[left]
        arr[pivot], arr[right] = arr[right], arr[pivot]
        return right
