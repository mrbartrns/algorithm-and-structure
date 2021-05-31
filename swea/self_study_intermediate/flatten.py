# 평탄화
def flatten(arr: list, counts) -> list:
    """
    arr: 1 dimension list which is sorted
    """
    i = 0
    while i < counts:
        arr[0] += 1
        arr[-1] -= 1
        left_swap(arr, 0, 1)
        right_swap(arr, len(arr) - 1, len(arr) - 2)
        i += 1
    return arr


def left_swap(arr, pre, cur):
    if cur < len(arr) and arr[pre] > arr[cur]:
        arr[pre], arr[cur] = arr[cur], arr[pre]
        done = left_swap(arr, pre + 1, cur + 1)
        return done
    else:
        return True


def right_swap(arr, pre, cur):
    if cur >= 0 and arr[pre] < arr[cur]:
        arr[pre], arr[cur] = arr[cur], arr[pre]
        done = right_swap(arr, pre - 1, cur - 1)
        return done
    else:
        return True


arr = [3, 2, 2, 3, 4, 5, 5, 6, 8, 8, 7]
print(flatten(arr, 4))