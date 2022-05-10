def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    left_idx = 0
    right_idx = 0
    ret = []
    # 두 배열을 비교하여 둘 중 작은 값을 새로운 배열에 삽입한다.
    # 이 과정이 끝나게되면 적어도 하나의 배열 내 요소들은 전부 새로운 배열에 삽입된다.
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            ret.append(left[left_idx])
            left_idx += 1
        else:
            ret.append(right[right_idx])
            right_idx += 1
    while left_idx < len(left):
        ret.append(left[left_idx])
        left_idx += 1
    while right_idx < len(right):
        ret.append(right[right_idx])
        right_idx += 1
    return ret


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(merge_sort(arr))
