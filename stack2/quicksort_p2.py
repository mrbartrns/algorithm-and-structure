def qs(arr, begin, end):
    if begin < end:
        p = partition(arr, begin, end)
        qs(arr, begin, p - 1)
        qs(arr, p + 1, end)
    

def partition(arr, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while arr[L] < arr[pivot] and L < R:
            L += 1
        while arr[R] >= arr[pivot] and L < R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            arr[L], arr[R] = arr[R], arr[L]
        arr[R], arr[pivot] = arr[pivot], arr[R]
    return R