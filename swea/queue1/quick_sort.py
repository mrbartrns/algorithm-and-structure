def qs(arr, begin, end):
    """
    pivot을 기준점으로 왼쪽과 오른쪽만 비교하면 된다.
    """
    if begin < end:
        p = partitian(arr, begin, end)
        qs(arr, begin, p - 1)
        qs(arr, p + 1, end)


def partitian(arr, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while arr[L] < arr[pivot] and L < R:
            L += 1
        while arr[R] >= arr[pivot] and L < R:
            R -= 1
        if L < R:
            if L == [pivot]:
                pivot = R
            arr[L], arr[R] = arr[R], arr[L]
        arr[R], arr[pivot] = arr[pivot], arr[R]
    return R
