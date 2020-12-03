def quickSort(arr, begin, end):
    if begin < end:
        p = partition(arr, begin, end)
        quickSort(arr, begin, p - 1)
        quickSort(arr, p + 1, end)


def partition(arr, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while arr[L] < arr[pivot] and L < R:
            L += 1
        while arr[R] >= arr[pivot] and L < R:
            R -= 1
        if L < R: # 두 인덱스가 아직 교차하지 않았다면
            if L == pivot:
                pivot = R # pivot과 R을 바꾸지 않게 하기 위함
            arr[L], arr[R] = arr[R], arr[L]
            print('L, R 교차:', arr)
        arr[pivot], arr[R] = arr[R], arr[pivot]
        print('pivot과 R 교차:', arr) # R과 피벗을 바꾸는 이유는 arr[pivot]이 항상 arr[R]보다 크기 때문에 pivot과 arr를 바꿔주는 것
        print('R:', R)
    return R # 새로운 기준점

arr = [68, 11, 29, 3, 15, 9, 32, 23]
quickSort(arr, 0, len(arr) - 1)
print(arr)


# def quickSort_primitive(arr):
    # if len(arr) == 1:
    #     return arr
    # else:
    #     pivot = arr[len(arr) // 2]
    #     lesser_arr, equal_arr, greater_arr = [], [], []
    #     for num in arr:
    #         if num < pivot:
    #             lesser_arr.append(num)
    #         elif num > pivot:
    #             greater_arr.append(num)
    #         else:
    #             equal_arr.append(num)
    #     return quickSort_primitive(lesser_arr) + equal_arr + quickSort_primitive(greater_arr)
